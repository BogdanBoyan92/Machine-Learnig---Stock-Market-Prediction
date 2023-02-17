import pickle
import os
from tensorflow import keras
import pandas as pd
import numpy as np

X_test = pd.read_csv("data/X_test_para_probar.csv")


with open('models/production/model', "rb") as modelo:
    carga_modelo = pickle.load(modelo)

pred_t = carga_modelo.predict(X_test)
pred_df = pd.DataFrame(pred_t)


pred_df.to_csv("data/Prediction_T")
