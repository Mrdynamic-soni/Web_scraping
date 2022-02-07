from importlib.resources import path
import os 

path = "C:\\Users\\Acer\\Desktop\\black_coffer"

os.chdir(path) #changing directory 
file_name = []
for file in os.listdir():  # read in folder
    if file.endswith(".txt"):
        file_name.append(file)

print(file_name)
