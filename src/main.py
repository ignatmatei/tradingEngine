import numpy as np
import pandas as pd
import tensorflow as tf
import os
i= 10
feature1=[]
feature2=[]
label =[]
while i < 31:
    if not os.path.exists('../data/trades202501' + str(i) + '.xlsx') :
        i += 1
        continue
    df = pd.read_excel('../data/trades202501' + str(i) + '.xlsx', engine='openpyxl', sheet_name = 0 , skiprows= 7, usecols = [7,8,9,10,11,12])
    if not os.path.exists('../data/trades202501' + str(i+1) + '.xlsx') :
        i += 1
        continue
    df_next_day = pd.read_excel('../data/trades202501' + str(i+1) + '.xlsx', engine='openpyxl', sheet_name = 0 , skiprows= 7, usecols = [7,8,9,10,11,12])

    #put all the stocks of the df in a dictionary
    stockNames = df['Indici / Indices']
    stockPrices = df['Unnamed: 8']
    stockPricesNextDay = df_next_day['Unnamed: 8']
    #only include 10 elements
    while len(stockNames) > 10:
        stockNames = stockNames[:-1]
        stockPrices = stockPrices[:-1]
        stockPricesNextDay = stockPricesNextDay[:-1]

    #drop first stock 
    stockNames = stockNames.drop(0)
    stockPrices = stockPrices.drop(0)
    stockPricesNextDay = stockPricesNextDay.drop(0)

    #convert to list
    stockNames = stockNames.tolist()
    stockPrices = stockPrices.tolist()
    stockPricesNextDay = stockPricesNextDay.tolist()

    j = 0
    while j < len(stockNames):
        feature1.append(stockPrices[j])
        feature2.append(stockPricesNextDay[j])
        if(stockPrices[j] < stockPricesNextDay[j]):
            label.append(1)
        else:
            label.append(0)
        j += 1
    i += 1
# standaedize the data
feature1 = (feature1 - np.mean(feature1)) / np.std(feature1)
feature2 = (feature2 - np.mean(feature2)) / np.std(feature2)

input1 = tf.keras.Input(shape=(1,))
input2 = tf.keras.Input(shape=(1,))
merged = tf.keras.layers.concatenate([input1, input2])

x = tf.keras.layers.Dense(32, activation='relu')(merged)
x = tf.keras.layers.Dropout(0.2)(x)
x = tf.keras.layers.Dense(16, activation='relu')(x)
x = tf.keras.layers.Dropout(0.2)(x)
x = tf.keras.layers.Dense(8, activation='relu')(x)
output = tf.keras.layers.Dense(1, activation='sigmoid')(x)  # Binary classification output

#Create the model
model = tf.keras.Model(inputs=[input1, input2], outputs=output)

#Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005), loss='binary_crossentropy', metrics=['accuracy'])
# Add early stopping
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

#Fit the model
model.fit([np.array(feature1), np.array(feature2)], np.array(label), epochs=100, batch_size=2, validation_split=0.2, callbacks=[early_stopping])

print(model.evaluate([np.array(feature1), np.array(feature2)], np.array(label)))
