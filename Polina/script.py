import os
import time
import datetime
import pandas as pd

df = pd.DataFrame()
df = pd.read_csv("/Users/max/Documents/ZebraHead22/Codes/test.csv", delimiter=',', index_col=None)
df["Время на занятии"] = (pd.to_datetime(df["Время выхода"], format='%d.%m.%Y %H:%M:%S %p') 
             - pd.to_datetime(df["Время входа"], format='%d.%m.%Y %H:%M:%S %p'))
df = df.rename(columns={'Имя (настоящее имя)': 'Name'})
df = df.set_index("Name")
df = df.groupby(level='Name').sum(numeric_only=False)
df = df.reset_index()
df["Минуты присутствия"] = df["Время на занятии"].dt.total_seconds().div(60).astype(int)

def normalise_row(row):
    if row["Минуты присутствия"] >= 55:
        result = "Зачет" 
    else:
        result = "Не зачет"  
    return result

df["Оценка присутствия"] = df.apply(lambda row : normalise_row(row), axis=1) 
print(df)