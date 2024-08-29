# In the current directory make some files, in some files add the word binod while in the others don't do it and when the program will run it wili tell which all files contain the word binod.

import os
import random

 #Code for changing os directory

# Code for creating files and writing content in them
# x = random.randint(0, 3)
# for i in range(15):
#     path = os.path.join(r"C:/Users/parth/Desktop/Codes/Python-practice-programs/txt-files-for-Program10", f"{i}-file.txt")
#     with open(path, 'w') as f:
#         if x==2:
#             f.write("Binod")
#         else:
            # f.write("kasjgil fiewfildfjdsl")

#Code for detecting binod

file_names=[]
os.chdir(r"C:\Users\parth\Desktop\Codes\Python-practice-programs\txt-files-for-Program10")
for i in os.listdir():
    path = os.path.join(r"C:\Users\parth\Desktop\Codes\Python-practice-programs\txt-files-for-Program10", f"{i}")
    with open(path, "r") as f:
        file_content = f.read()
        if "Binod" in file_content:
            file_names.append(i)
        else:
            continue

print("Files having the word 'Binod' in them:")
for i in file_names:
    print(i, end=", ")
