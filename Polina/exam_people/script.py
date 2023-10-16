import os
import time
import csv
import datetime
import pandas as pd

df = pd.read_excel('/Users/max/Documents/ZebraHead22/Polina/files/test.xlsx', index_col=None)
df2 = df.iloc[:, 0].str.split(',', expand=True)
print(df2)
df2.columns = [n.replace('"', '') for n in df.columns.str.split(',')[0]]
print(df2)