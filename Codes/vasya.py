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


