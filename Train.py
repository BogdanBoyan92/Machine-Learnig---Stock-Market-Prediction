import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM,Dropout,Dense
from tensorflow import keras
import pickle
from datetime import datetime
import os

dir_script = os.path.dirname(os.path.abspath(__file__))

Train_df = pd.read_csv("data/Train.csv", index_col="Date")

final_dataset = Train_df.values

train_data = final_dataset[0:2000, :]
valid_data = final_dataset[2000: , :]

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(final_dataset)

days = 60
X_train_data, y_train_data = [], []

for i in range(days, len(train_data)):
    X_train_data.append(scaled_data[i-days:i, 0])
    y_train_data.append(scaled_data[i, 0])

X_train_data, y_train_data =np.array(X_train_data), np.array(y_train_data)
X_train_data = np.reshape(X_train_data, (X_train_data.shape[0], X_train_data.shape[1], 1))    

lstm_model = Sequential()
lstm_model.add(LSTM(units=50, return_sequences=True, input_shape = (X_train_data.shape[1], 1)))
lstm_model.add(Dropout(0.2))

lstm_model.add(LSTM(units=50))
lstm_model.add(Dropout(0.2))
lstm_model.add(Dense(1))

lstm_model.compile(loss="mean_squared_error", optimizer="adam")
lstm_model.fit(X_train_data, y_train_data, epochs=10, batch_size=500, verbose=2)

now = datetime.now()
anio = now.strftime('%Y')[2:]
timestamp = anio + now.strftime('%m%d%H%M%S')

filename = dir_script + '/models/model' + timestamp
with open(filename, 'wb') as archivo_salida:
    pickle.dump(lstm_model, archivo_salida)

filename = dir_script + '/models/production/model' 
with open(filename, "wb") as archivo_salida:
    pickle.dump(lstm_model, archivo_salida)

