#
# Lance une boucle de test sur le modèle et sur la regression
# Paramètres testés :
#    ilots = ["ilot1", "all"]
#    sensors = ["co2", "hum", "lum", "temp"]
#    intervals = [3600, 300]
#    configs = [(2,1), (16,4), (32,16)] <- des paires (serie_length, to_predict)

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import sklearn.metrics as metrics
from tslearn.metrics import dtw, cdist_dtw

# Confort functions
import annotationUnique as anno

# Le modèle
from training import MartyModel as MM
from training import load_data, split_data





def write_csv_header(file, sep=';'):
    """Erase 'file' and write the header line"""
    with open(file, 'w') as f:
        f.write("name;ilot;sensor;interval;n_samples;train_set_size;serie_length;to_predict;overlap;absolute_error;mean_squared_error;dtw_dist;accuracy;f-measure;jaccard\n")


def write_csv_line(file, name, ilot, sensor, interval, n_samples,
                   train_set_size, serie_length,
                   to_predict, overlap, abs_err, ms_err,
                   dtw_d, accu, fmeas, jacc, sep=";"):
    """Append a line into 'file'"""
    with open(file, 'a') as f:
        f.write(sep.join([str(x) for x in [name, ilot, sensor,
                                           interval, n_samples,
                                           train_set_size, serie_length,
                                           to_predict, overlap,
                                           abs_err, ms_err, dtw_d,
                                           accu, fmeas, jacc]]
                         ) + "\n")





def split_datasets(X, y, timestamps):

    # Method from 'training.py'
##                    train_set, dev_set, test_set, timestamps = split_data(X, y, timestamps)
##                    X_train, y_train = train_set
##                    X_dev, y_dev = dev_set
##                    X_test, y_test = test_set

    
    # Method from sklearn
    # random_state = 43 : we can re-use trained models without
    # mixing train-set and test-set
    X_train, X_test, y_train, y_test, ts_train, ts_test = train_test_split(X, y, timestamps, test_size=0.2, random_state=43)
    X_dev, X_test, y_dev, y_test, ts_dev, ts_test = train_test_split(X_test, y_test, ts_test, test_size=0.5, random_state=43)

    return (X_train,y_train), (X_dev,y_dev), (X_test,y_test), ts_test







        


def test_models(ilot, sensor, interval, serie_length, to_predict):
    "Teste le modèle et la regression linéaire pour les paramètres donnés"""

    # Instanciate models to test
    k = ".".join([str(x) for x in [ilot, sensor, interval, serie_length, to_predict]])

    models = {
        k+".LSTM64-ReLU16-Sigm1": MM(serie_length, to_predict),
        k+".LinearRegression": LinearRegression()
        }

    # Load data
    # NE SUPPORTE PAS LES NANS
    data_filename = "{}.{}.{}.csv".format(ilot, sensor, interval)
    data_path = os.path.join(os.path.dirname(sys.argv[0]), "..", "data", "output", data_filename)
    X, y, timestamps, Yminmax = load_data(
        data_path,
        serie_length = serie_length,
        to_predict = to_predict,
        overlap = True
        )

    # Reserve n contiguous points for visualisation
    # n = points for a week
    n = int(7 * 86400 / interval)
    X, X_visu, y, y_visu, timestamps, timestamps_visu = train_test_split(
        X, y, timestamps, test_size=n, shuffle=False)
    visu_set = X_visu, y_visu

    # Split data into train, dev and test sets
    train_set, dev_set, test_set, timestamps = split_datasets(X, y, timestamps)
    X_train, y_train = train_set
    X_dev, y_dev = dev_set
    X_test, y_test = test_set

    # Limit train_set to 10000 elements
    if len(X_train) > 10000:
        X_train = X_train[:10000]
        y_train = y_train[:10000]
        train_set = X_train, y_train

    # Limit dev_set to 1000 elements
    if len(X_dev) > 1000:
        X_dev = X_dev[:1000]
        y_dev = y_dev[:1000]
        dev_set = X_dev, y_dev

    # tensors for LSTMs
    X_train = np.expand_dims(X_train, axis=-1)
    X_dev = np.expand_dims(X_dev, axis=-1)
    X_test = np.expand_dims(X_test, axis=-1)
    X_visu = np.expand_dims(X_visu, axis=-1)



    for name, model in models.items():

        print("\nEvaluate", name, file=sys.stderr)
        print("\nEvaluate", name)

        model_filename = os.path.join(os.path.dirname(sys.argv[0]),'models', name+'.h5')
   

        # Fit LSTM model
        if name.endswith("Sigm1"):

            model.fit(X_train, y_train,
                      X_dev, y_dev,
                      compile_model=(not os.path.isfile(model_filename)),
                      save_path=model_filename)
            y_pred = model.predict(X_test)
            y_pred_visu = model.predict(X_visu)

        # Fit linear regression model
        else:
            model.fit(*train_set)
            y_pred = model.predict(test_set[0])
            y_pred_visu = model.predict(visu_set[0])



        # Plot test_set prediction and truth
        print("Plot test-set", file=sys.stderr)
        save_figs(file = os.path.join("eval_output","complete."+name+".png"),
                  X = timestamps,
                  y = y_test,
                  y_pred = y_pred,
                  title = name,
                  interp = Yminmax
                  )

        # Plot reserved contiguous points
        print("Plot visu-set", file=sys.stderr)
        save_figs(file = os.path.join("eval_output","contiguous."+name+".png"),
                  X = timestamps_visu,
                  y = y_visu,
                  y_pred = y_pred_visu,
                  title = name,
                  interp = Yminmax
                  )

        # Plot and scatter 50 points
        print("Plot 50 contiguous points", file=sys.stderr)
        n_points = 50
        if len(y_pred_visu) > n_points:
            save_figs(file = os.path.join("eval_output","contig"+str(n_points)+"."+name+".png"),
                      X = timestamps_visu[-n_points:],
                      y = y_visu[-n_points:],
                      y_pred = y_pred_visu[-n_points:],
                      title = name,
                      interp = Yminmax,
                      scatter = True
                      )
        




        # Scores to 1D
        y_pred = y_pred.reshape((y_pred.shape[0],))
        y_test = y_test.reshape((y_test.shape[0],))
        
        # To confort score
        print("Confort conversion", file=sys.stderr)
        funcs = {
            'co2': lambda x: anno.co2(x),
            'hum': lambda x: anno.humidite(x),
            'lum': lambda x: anno.luminosite(x),
            'temp':lambda x: anno.temperature(x)
            }
        f = np.vectorize(funcs[sensor])
        confort = f(np.interp(y_test, (0,1), Yminmax))
        confort_pred = f(np.interp(y_pred, (0,1), Yminmax))


        # Regression
        # Absolute error: measures accuracy
        print("Compute absolute error", file=sys.stderr)
        abs_err = metrics.mean_absolute_error(y_test, y_pred)
        
        # Mean squared error: measures accuracy, penalizing bad forecast points
        print("Compute mean error", file=sys.stderr)
        ms_err = metrics.mean_squared_error(y_test, y_pred)

        # DTW distance: series alignment (too long to compute)
        print("Compute DTW distance", file=sys.stderr)
        dtw_d = "not computed" #dtw(y_test, y_pred)

        # Classification
        # Accuracy (with confort score)
        print("Compute accuracy", file=sys.stderr)
        accuracy = metrics.accuracy_score(confort, confort_pred)

        # F-measure (with confort score)
        print("Compute F1-score (micro)", file=sys.stderr)
        fmeasure = metrics.f1_score(confort, confort_pred, average="micro")

        # Jaccard similary
        print("Compute Jaccard similarity", file=sys.stderr)
        jaccard = metrics.jaccard_similarity_score(confort, confort_pred)



        # Write scores into csv
        write_csv_line("evaluation.csv", name.split(".")[-1],
                       ilot, sensor, interval,
                       len(X_train)+len(X_dev)+len(X_test),
                       len(X_train),
                       serie_length, to_predict, 1,
                       abs_err, ms_err, dtw_d,
                       accuracy, fmeasure, jaccard)

        # Write matrices into stdout
        print("Accuracy confusion matrix (confort)")
        print(metrics.confusion_matrix(confort, confort_pred))

##        print("DTW confusion matrix (values)")
##        print(cdist_dtw(y_test, y_pred))
        






    
def save_figs(file, X, y, y_pred, title="", interp=None, scatter=False):
    """Save a plot of results (truth and prediction)"""
    X = X.reshape((X.shape[0]))
    y = y.reshape((y.shape[0]))
    y_pred = y_pred.reshape((y_pred.shape[0]))

    # Sort X, y and y_pred together along X
    points = np.ndarray((X.shape[0], 3))
    points[:,0] = X
    points[:,1] = y
    points[:,2] = y_pred
    points = points[points[:,0].argsort()]
    X = points[:,0]
    y = points[:,1]
    y_pred = points[:,2]

    plt.title(title)

##    print("shapes", X.shape, y.shape, y_pred.shape)

    if interp is not None:
        y = np.interp(y, (0,1), interp)
        y_pred = np.interp(y_pred, (0,1), interp)
                    
    plt.plot(X, y, label="truth")
    plt.plot(X, y_pred, label="prediction")

    if scatter:
        plt.scatter(X, y)
        plt.scatter(X, y_pred)


    plt.xlabel("timestamp")
    plt.ylabel("value")
    plt.legend()

    plt.savefig(file)
    plt.close()




def main():

    # We compare our model with LinearRegression and knn (when classifying)
    # We use <i>.<s>.<t> datasets, with :

    ilots = ["ilot1", "all"]
    sensors = ["co2", "hum", "lum", "temp"]
    intervals = [3600, 300]
    configs = [(2,1), (16,4), (32,16)]


    write_csv_header("evaluation.csv")

    for ilot in ilots:
        for serie_length, to_predict in configs: 
            for sensor in sensors:
                for interval in intervals:
##                    try:
##                        train_model(ilot, sensor, interval, serie_length, to_predict)
                        test_models(ilot, sensor, interval, serie_length, to_predict)
##                    except Exception as e:
##                        print("Model was not train, an error has occured")
##                        print("serie_length:", serie_length)
##                        print("to_predict:", to_predict)
##                        print("ilot:", ilot)
##                        print("sensor:", sensor)
##                        print("interval:", interval)
##                        print(e)
                        


    exit(0)



if __name__ == "__main__":
    main()

