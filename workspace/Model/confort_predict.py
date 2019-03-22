#!/usr/bin/env python
# coding: utf-8

# VERSION OBSOLETE, PRENEZ test_val_conf.py #

# VERSION OBSOLETE, PRENEZ test_val_conf.py #

# VERSION OBSOLETE, PRENEZ test_val_conf.py #

# VERSION OBSOLETE, PRENEZ test_val_conf.py #

# VERSION OBSOLETE, PRENEZ test_val_conf.py #

# VERSION OBSOLETE, PRENEZ test_val_conf.py #

# VERSION OBSOLETE, PRENEZ test_val_conf.py #

# VERSION OBSOLETE, PRENEZ test_val_conf.py #

import numpy as np
from keras.models import load_model, Model
from annotationUnique import annotationCapteur

# ### Current values

# ceci est un test

actual_temp = np.ndarray(30, dtype = "float32")
actual_temp.fill(0.30) # (11.36, 40.0)

actual_co2 = np.ndarray(30, dtype = "float32")
actual_co2.fill(0.3) # (84, 1990)

actual_lum = np.ndarray(90, dtype = "float32")
actual_lum.fill(0.6) # (0, 1000)

actual_hum = np.ndarray(30, dtype = "float32")
actual_hum.fill(0.7) # (min, max) : (30,75)

actual_features = [actual_co2, actual_hum, actual_lum, actual_temp]

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


print(annotationCapteur(
    Y_test_pred2.mean() * 28.64 + 11.36, Y_test_pred3.mean() * 1000 + 0, 
    Y_test_pred1.mean() * 1906 + 84, Y_test_pred4.mean() * 45 + 30))

