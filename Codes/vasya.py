import os
import time
import datetime
import pandas as pd

def rename_video():
    '''
    Переименовываем видео файлы, записывая дату создания
    в имя
    '''
    direct = os.getcwd()
    files = os.listdir(direct)
    for i in files:
        filename, file_extension = os.path.splitext(i)
        if file_extension == ".MOV":
            new_name = time.ctime(os.path.getmtime(i))
            os.rename(i, direct+"/"+str(new_name)+".MOV")


def new_131023():
    pass
    # files = os.listdir(os.getcwd())
    # people = pd.DataFrame()
    # for file in files:
    #     filename, file_extension = os.path.splitext(file)
    #     if file_extension == ".xlsl":
    #         df = pd.read_csv(file, delimer = ",", index_col = None)
    #         print(df)

df = pd.DataFrame()
df1 = pd.DataFrame()
df = pd.read_csv("/Users/max/Documents/ZebraHead22/Codes/test.csv", delimiter=',', index_col=None)
df['Время входа'] = pd.to_datetime(df['Время входа'], format='%d.%m.%Y %H:%M:%S %p')
df['Время выхода'] = pd.to_datetime(df['Время выхода'], format='%d.%m.%Y %H:%M:%S %p')
df["SUM"] = (pd.to_datetime(df["Время выхода"]) - pd.to_datetime(df["Время входа"]))
df1["Name"] = df["Имя (настоящее имя)"]
df1["video_time"] = df["SUM"]
df1 = df1.set_index("Name")
# df1 = df1.groupby(level='video_time').sum()
# df1 = df1.reset_index()

print(df1)