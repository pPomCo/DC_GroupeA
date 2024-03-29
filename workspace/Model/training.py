import sys
import keras.layers as kl
import keras.backend as K
import keras.callbacks as kc
from keras.models import Sequential, load_model, Model

from sklearn import linear_model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics

import os
import tensorflow as tf




def load_data(filename, serie_length, to_predict=1, overlap=False):

    # Identity sensor from filename
    sensor = os.path.basename(filename).split('.')[1]
    assert sensor in ['co2','hum','lum','temp']

    # to get inputs whatever the OS
    data = pd.read_csv(filename, sep= ";")

    data.head()

    # # Prepare data

    values = data[sensor].values
    timestamps = data["timestamp"].values

    # remove beginning
    nb_todelete = len(values) % serie_length
    values = values[nb_todelete:]
    timestamps = timestamps[nb_todelete:]

    # create X and Y
    # X.shape = (n, serie_length)   X[i,j] = values[i+j]
    # Y.shape = (n,)                Y[i] = mean( X[i+to_predict,:] )
    # n = len(values) - (serie_length * to_predict)
    if overlap:
        step = 1
    else:
        step = serie_length
    X, Y = [], []
    for i in range(0, len(values) - (serie_length * to_predict), step):
        window = values[i : i + serie_length]
        next_window = values[i + serie_length * to_predict : i + serie_length * (to_predict + 1)]
        X.append(window)
        Y.append(next_window.mean())
    
    X = np.array(X)
    Y = np.array(Y)
    timestamps = np.array(timestamps[serie_length * to_predict::step])


    # Valeurs de Y[i] OK (égales à la moyenne des X[i+to_predict] )
##    for i, x in enumerate(X[:5]):
##        print(*x, Y[i])

        
    # Normalisation entre min et max vers des valeurs de 0 à 1
    Yminmax = Y.min(), Y.max()
    X = np.interp(X, (X.min(), X.max()), (0, 1))
    Y = np.interp(Y, (Y.min(), Y.max()), (0, 1))

    # Valeurs de Y[i] KO (différentes de la moyenne des X[i+to_predict] )
##    for i, x in enumerate(X[:5]):
##        print(*x, Y[i])


##    print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)

    return X, Y, timestamps, Yminmax




def split_data(X, Y, timestamps, ratio_train_dev=0.8, ratio_dev_test=0.1):
    # split between training and validation
    ratio_train_dev = 0.8
    ratio_dev_test = 0.1
    split_index_1 = int(len(X) * ratio_train_dev)
    split_index_2 = int(len(X) * (ratio_train_dev + ratio_dev_test))

    X_train, X_dev, X_test = X[ : split_index_1], X[split_index_1 : split_index_2], X[split_index_2 : ]
    Y_train, Y_dev, Y_test = Y[ : split_index_1], Y[split_index_1 : split_index_2], Y[split_index_2 : ]
    timestamps_test = timestamps[split_index_2:]
    
    # cause LSTM wants 3d vectors
    X_train = np.expand_dims(X_train, axis=-1)
    X_dev = np.expand_dims(X_dev, axis=-1)
    X_test = np.expand_dims(X_test, axis=-1)
    
    return (X_train, Y_train), (X_dev, Y_dev), (X_test, Y_test), timestamps_test







class KerasModel(object):

    def __init__(self, serie_length, to_predict, name="model-dev"):
        self.serie_length = serie_length
        self.to_predict = to_predict
        self.model_name = "models/{}.h5".format(name)


    def fit(self, X_train, Y_train, X_dev, Y_dev, compile_model=True, save_path=None):

        if save_path is None:
            save_path = self.model_name

        if compile_model:

            # Sequential way to define model
            # model = Sequential()
            # model.add(kl.Input(X_train[0].shape))
            # model.add(kl.LSTM(16))
            # model.add(kl.Dense(1, activation="sigmoid"))
            # model.compile(loss = 'mse', optimizer = 'adam')
            # model.summary()

            # Recusive way to define rnn
            neural_network_input = kl.Input(X_train[0].shape)

            recursive_neural_network = kl.GRU(64)(neural_network_input)
            # recursive_neural_network = kl.LSTM(64)(neural_network_input) # LSTM : worse prediction than GRU in that case
            # recursive_neural_network = kl.CuDNNGRU(64)(neural_network_input) # for nvidia (way way faster)

            dense = kl.Dense(16, activation = "relu")(recursive_neural_network)
            dense = kl.Dense(1, activation = "sigmoid")(dense)

            model = Model(inputs = [neural_network_input], outputs = [dense])
            model.summary()

            model.compile(loss = "mse", optimizer = "adam")


            # permet d'arrêter le training avant la fin si rien n'est améliorer en 10 epochs
            early_stop = kc.EarlyStopping(monitor = 'val_loss', patience = 10, verbose = 1, mode = 'min')
            # enregistre le modèle si le val_loss est meilleur que l'actuel meilleur modèle
            checkpoint = kc.ModelCheckpoint(save_path, monitor = 'val_loss', verbose = 1, save_best_only = True, mode = 'min')
            # permet de revenir en arrière si rencontre avec un min local en reduisant le LR
            reduce_lr = kc.ReduceLROnPlateau(monitor = 'val_loss', factor = 0.25, patience = 25, verbose = 1, mode = 'min', min_lr = 1e-6)

            callbacks = [early_stop, checkpoint, reduce_lr]

            history = model.fit(
                X_train, Y_train,
                validation_data = (X_dev, Y_dev),
                epochs = 20,
                batch_size = 16,
                callbacks = callbacks
            )
            
        self.model = load_model(save_path)



    def predict(self, X):
        return self.model.predict(X)

    def score(self, X, Y):
        return self.model.evaluate(X, Y)

class LinearModel(object):
    def __init__(self, serie_length, to_predict):
        self.serie_length = serie_length
        self.to_predict = to_predict

        self.model = linear_model.LinearRegression()

    def fit(self, X_train, Y_train, X_dev, Y_dev):
        self.model.fit(X_train.reshape((-1, self.serie_length)), Y_train)

    def predict(self, X):
        return self.model.predict(X.reshape((-1, self.serie_length)))

    def score(self, X, Y):
        return ((self.predict(X) - Y)**2).mean()

if __name__ == "__main__":

    # argv ?
    filename = "ilot1.temp.300.csv"
    path = os.path.join(os.path.dirname(sys.argv[0]), "..", "data", "output", filename)
    serie_length = 4
    to_predict = 2
    name = "model-dev"
    compile_model = False

    # Load data
    X, Y, timestamps, Yminmax = load_data(path, serie_length, to_predict)
    train_set, dev_set, test_set, timestamps = split_data(X, Y, timestamps, 0.8, 0.1)

    # Instanciate model
    m = KerasModel(serie_length, to_predict, name)
    m_linear = LinearModel(serie_length, to_predict)

    # Fit data
    m.fit(*train_set, *dev_set, compile_model=compile_model)
    m_linear.fit(*train_set, *dev_set)

    # Predict
    X_test, Y_test = test_set
    Y_test_pred = m.predict(X_test)
    Y_linear_pred = m_linear.predict(X_test)

    print("LinearRegression :", m_linear.score(X_test, Y_test))
    print("KerasModel :", m.score(X_test, Y_test))

    # Plot
    plt.plot(timestamps, np.interp(Y_test, (0,1), Yminmax),
        label="truth", alpha=0.8)
    plt.plot(timestamps, np.interp(Y_test_pred, (0,1), Yminmax), 
        '--', label="prediction", alpha=0.8)
    plt.plot(timestamps, np.interp(Y_linear_pred, (0,1), Yminmax), 
        '--', label="linear", alpha=0.8)
    
    plt.xlabel("timestamp")
    plt.ylabel("value")
    plt.legend()

    plt.show()
    plt.close()                   
