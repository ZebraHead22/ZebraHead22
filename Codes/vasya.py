import os
import time

direct = os.getcwd()
files = os.listdir(direct)
for i in files:
    filename, file_extension = os.path.splitext(i)
    if file_extension == ".MOV":
        new_name = time.ctime(os.path.getmtime(i))
        os.rename(i, direct+"/"+str(new_name)+".MOV")