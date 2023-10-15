import os
import time
import csv
import datetime
import pandas as pd

df = pd.read_csv('/Users/max/Documents/ZebraHead22/Polina/test.csv',
                 delimiter=',', index_col=None)
df['Время на занятии'] = (pd.to_datetime(df['Время выхода'], format='%d.%m.%Y %H:%M:%S %p')
                          - pd.to_datetime(df['Время входа'], format='%d.%m.%Y %H:%M:%S %p'))
df = df.rename(columns={'Имя (настоящее имя)': 'Name'})
df = df.set_index('Name')
df = df.sort_index()
df = df.reset_index()

names = df['Name'].to_list()

def rename(lst):
    for i in range(len(lst)-1):
        if lst[i] != 'iPhone':
            if str(lst[i+1]).count(lst[i]) >= 1:
                lst[i+1] = lst[i]
    return lst

rename(names)

df['Name'] = names
df = df.set_index('Name')
df = df.groupby(level='Name').sum(numeric_only=False)
df = df.reset_index()
df['Минуты присутствия'] = df['Время на занятии'].dt.total_seconds().div(60).astype(int)

def normalise_row(row):
    if row['Минуты присутствия'] >= 55:
        result = 'Зачет'
    else:
        result = 'Не зачет'
    return result

df['Оценка присутствия'] = df.apply(lambda row: normalise_row(row), axis=1)
df = df.drop(['Электронная почта пользователя', 'Время входа', 'Время выхода', 'Продолжительность (минуты)',
             'Гость', 'Согласие на запись', 'В зале ожидания', 'Время на занятии'], axis=1)
with pd.ExcelWriter('/Users/max/Documents/ZebraHead22/Polina/result.xlsx') as writer:
    df.to_excel(writer, sheet_name='Lesson',
                index=None, index_label=None)
