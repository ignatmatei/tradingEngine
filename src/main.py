import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

i= 28
df = pd.read_excel('../data/trades202501' + str(i) + '.xlsx', engine='openpyxl', sheet_name = 0 , skiprows= 7, usecols = [7,8,9,10,11,12])

#put all the stocks of the df in a dictionary
stocks = df['Indici / Indices']

print(stocks)
