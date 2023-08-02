import os
import shutil

source = r"C:\Users\rskch\Desktop\Python\Project 102"
destination = r"C:\Users\rskch\Desktop\Python\Project 102\Words"

list_of_files = os.listdir(source)
print(list_of_files)

for x in list_of_files:
    name,extention = os.path.splitext(x)
    if (extention == ""):
        continue
    if extention in [".docx",".pdf",".txt"]:
        path1 = source + "/" + x
        path2 = destination 
        path3 = destination + "/" + x
        if os.path.exists(path2):
            print("The folder already exists")
            shutil.move(path1,path3)
        else:
            print("Creating a new folder")
            os.mkdir(path2)
            print("Moving the files")
            shutil.move(path1,path3)
