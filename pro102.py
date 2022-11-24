import os
import shutil
from_dir = "C:/Users/acer/Downloads"
to_dir = "C:/Users/acer/Desktop/python folder/documents"
list_of_files = os.listdir(from_dir)
#print(list_of_files)
for file in list_of_files:
    name,extension = os.path.splitext(file)
    #print(extension)
    if extension == '':
        continue
    if extension in [".txt",".doc",".docx",".pdf"]:
        path1 = from_dir + "/" + file
        path2 = to_dir
        path3 = to_dir + "/" + file
        if os.path.exists(path2):
            print("Moving.....")
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("Moving....")
            shutil.move(path1,path3)