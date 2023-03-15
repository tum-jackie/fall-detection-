# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qWVgfADG7hSi33SbUbmEh3-amXocSjDs
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load data
data = pd.read_csv('/content/drive/MyDrive/SisFall_dataset.csv/SisFall_dataset.csv',usecols =[0,1,2,9])
print(data)

# from sklearn.preprocessing import StandardScaler
# X = data.iloc[:, :-1].values
# scaler = StandardScaler()
# X = scaler.fit_transform(X) # Normalize
# y = data.iloc[:, -1]



# X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

import numpy as np


# Split into features (X) and labels (y)
X = data[['ADXL345_x', 'ADXL345_y', 'ADXL345_z']].values
y = data.iloc[:, -1]

# Convert labels to binary values (0 = not fall, 1 = fall)
y_binary = np.zeros_like(y)
y_binary[y == 'fall'] = 1

#Split into training and validation sets
split = 0.8
split_idx = int(len(X) * split)
X_train = X[:split_idx]
X_val = X[split_idx:]
y_train = y_binary[:split_idx]
y_val = y_binary[split_idx:]

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dropout

# Build model with regularization
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(3,), kernel_regularizer=tf.keras.regularizers.l2(0.001)),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(64, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001)),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
# Compile model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train model
model.fit(X_train, y_train.astype('float32'), epochs=5 ,validation_data=(X_val, y_val.astype('float32')))

loss, accuracy = model.evaluate(X_train, y_train.astype('float32'))
print(f'Loss: {loss}, Accuracy: {accuracy}')

#save the trained tensorflow model
model.save('fall_detection_model.h5')

from google.colab import files
#convert the tensorflow model to tflite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
open("fall_detection_model.tflite", "wb").write(tflite_model)
files.download('fall_detection_model.tflite')