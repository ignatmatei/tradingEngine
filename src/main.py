import pandas as pd

df = pd.read_excel('../data/trades20250128.xlsx', engine='openpyxl', sheet_name = 0 , skiprows= 7, usecols = [7,8,9,10,11,12])

print(df)
