import sys

if(len(sys.argv) < 4) :
	print("Usage : script.py ilot feature serie_length")
	# ilot1 lum 30
	# ilot1 temp 10
	# ilot1 hum 10
	# ilot1 co2 10
	exit(1)

import keras.layers as kl
import keras.backend as K
import keras.callbacks as kc
from keras.models import Sequential, load_model, Model

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics

import os
import tensorflow as tf




# variables d'environnement

location = sys.argv[1]
feature = sys.argv[2]

file_name = str(location) + "." + str(feature) + ".csv"


serie_length = sys.argv[3] # nbr of data taken for training set
to_predict = 1 # how far to predict (nbr of serie_length far)
# rq : the further we try to predict, the inaccurate results are, obviously true

# # Load data


# to get inputs whatever the OS
data_root = os.path.join(".", "Formatage", "parts")
data = pd.read_csv(os.path.join(data_root, file_name), sep= ";")

data.head()


# # Prepare data

values = data["value"].values


# remove beginning
nb_todelete = len(values) % serie_length
values = values[nb_todelete:]

# create X and Y
X, Y = [], []
for i in range(0, len(values) - (serie_length * to_predict), serie_length):
    window = values[i : i + serie_length]
    next_window = values[i + serie_length * to_predict : i + serie_length * (to_predict + 1)]
    
    X.append(window)
    Y.append(next_window.mean())

X = np.array(X)
Y = np.array(Y)
# X.shape, Y.shape


# Normalisation entre min et max vers des valeurs de 0 à 1
X = np.interp(X, (X.min(), X.max()), (0, 1))
Y = np.interp(Y, (Y.min(), Y.max()), (0, 1))


# split between training and validation
ratio = 0.8
split_index = int(len(X) * ratio)

X_train, X_test = X[:split_index], X[split_index:]
Y_train, Y_test = Y[:split_index], Y[split_index:]

# cause LSTM wants 3d vectors
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)

# X_train.shape, X_test.shape, Y_train.shape, Y_test.shape


# # Training

# K.clear_session() # avoid jupyter burnout
model_name = "models/model_" + file_name[:-4] + "_" + str(serie_length) + "_" + str(to_predict) + ".h5"

# Sequential way to define model
# model = Sequential()
# model.add(kl.Input(X_train[0].shape))
# model.add(kl.LSTM(16))
# model.add(kl.Dense(1, activation="sigmoid"))
# model.compile(loss = 'mse', optimizer = 'adam')
# model.summary()

# Recusive way to define model
inp = kl.Input(X_train[0].shape)
rnn = kl.LSTM(64)(inp)
#rnn = kl.CuDNNGRU(64)(inp) # for nvidia (way way faster)

dense = kl.Dense(16, activation = "relu")(rnn)
dense = kl.Dense(1, activation = "sigmoid")(dense)

model = Model(inputs = [inp], outputs = [dense])
model.summary()

model.compile(loss="mse", optimizer="adam")


# permet d'arrêter le training avant la fin si rien n'est améliorer en 10 epochs
early_stop = kc.EarlyStopping(monitor='val_loss', patience=10, verbose=1, mode='min')
# enregistre le modèle si le val_loss est meilleur que l'actuel meilleur modèle
checkpoint = kc.ModelCheckpoint(model_name, monitor='val_loss', verbose=1, save_best_only=True, mode='min')
# permet de revenir en arrière si rencontre avec un min local en reduisant le LR
reduce_lr = kc.ReduceLROnPlateau(monitor='val_loss', factor=0.25, patience=25, verbose=1, mode='min', min_lr=1e-6)

callbacks = [early_stop, checkpoint, reduce_lr]

history = model.fit(
    X_train, Y_train,
    validation_data = (X_test, Y_test),
    epochs = 10,
    batch_size = 32,
    callbacks = callbacks
)

model = load_model(model_name)
Y_test_pred = model.predict(X_test)


# # Data Representation

plt.figure(0, figsize = (20, 6))

plt.hist(Y_test, bins = 20) # blue : actual data
plt.hist(Y_test_pred, bins = 20) # orange : predicted data
plt.show()


plt.figure(0, figsize = (20, 6))
plt.plot(sorted(Y_test))
plt.plot(sorted(Y_test_pred))

plt.show()


error_is = 100 * sklearn.metrics.mean_squared_error(Y_test, Y_test_pred)
print("errors : " + str(error_is.round(4)))

