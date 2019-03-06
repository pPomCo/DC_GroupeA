#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from keras.models import load_model, Model
from annotationUnique import annotationCapteur
import os

# ### Current values

data_root = os.path.join(".", "current_data") # to get inputs whatever the OS

actual_temp = np.ndarray(30, dtype = "float32") # (11.36, 40.0)
with open("current_data/temp.txt") as file: # Use file to refer to the file object
	data = file.read().split(";")
	data = [float(d) for d in data]
actual_temp = np.interp(data, (11.36, 40), (0, 1))

actual_co2 = np.ndarray(30, dtype = "float32") # (84, 1990)
with open("current_data/co2.txt") as file: # Use file to refer to the file object
	data = file.read().split(";")
	data = [float(d) for d in data]
actual_co2 = np.interp(data, (84, 1990), (0, 1))

actual_lum = np.ndarray(30, dtype = "float32") # (0, 1000)
with open("current_data/lum.txt") as file: # Use file to refer to the file object
	data = file.read().split(";")
	data = [float(d) for d in data]
actual_lum = np.interp(data, (0, 1000), (0, 1))

actual_hum = np.ndarray(30, dtype = "float32") # (min, max) : (30,75)
with open("current_data/hum.txt") as file: # Use file to refer to the file object
	data = file.read().split(";")
	data = [float(d) for d in data]
actual_hum = np.interp(data, (30, 75), (0, 1))

actual_features = [actual_co2, actual_hum, actual_lum, actual_temp]

# les valeurs sont preditent sur [0, 1] donc il faut faire l'interpolation inverse (ici faite manuellement)
print("Confort actuel : " + annotationCapteur(	actual_features[1].mean() * 28.64 + 11.36, 
actual_features[2].mean() * 1000 + 0, actual_features[0].mean() * 1906 + 84, actual_features[3].mean() * 45 + 30)[:3])

# actual_temp, actual_co2, actual_lum, actual_hum

model_name_1 = "models/model_ilot1.co2_10_1.h5"
model_name_2 = "models/model_ilot1.temp_10_1.h5"
model_name_3 = "models/model_ilot1.lum_30_1.h5"
model_name_4 = "models/model_ilot1.hum_10_1.h5"


model1 = load_model(model_name_1)
Y_test_pred1 = model1.predict(actual_co2.reshape(3,10,1))

model2 = load_model(model_name_2)
Y_test_pred2 = model2.predict(actual_temp.reshape(3,10,1))

model3 = load_model(model_name_3)
Y_test_pred3 = model3.predict(actual_lum.reshape(3,30,1))

model4 = load_model(model_name_4)
Y_test_pred4 = model4.predict(actual_hum.reshape(3,10,1))


Y_test_pred1, Y_test_pred2, Y_test_pred3, Y_test_pred4


# # prediction de la valeur de confort

# les valeurs sont preditent sur [0, 1] donc il faut faire l'interpolation inverse (ici faite manuellement)
print("Confort prédit : " + annotationCapteur(
    Y_test_pred2.mean() * 28.64 + 11.36, Y_test_pred3.mean() * 1000 + 0, 
    Y_test_pred1.mean() * 1906 + 84, Y_test_pred4.mean() * 45 + 30)[:3])

