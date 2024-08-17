#You have different types of files in a folder, create folders for different extentions and place the files in them


import os
from shutil import move

x = os.listdir() #List of all the files in this directory
for i in os.listdir():
    if i.endswith(".txt"):
        if os.path.isdir("C:/Users/parth/Desktop/Codes/Python-practice-programs/txt"):
            move(i, "C:/Users/parth/Desktop/Codes/Python-practice-programs/txt")
        else:
            os.mkdir("C:/Users/parth/Desktop/Codes/Python-practice-programs/txt")
            move(i, "C:/Users/parth/Desktop/Codes/Python-practice-programs/txt")
            
    elif i.endswith(".docx"):
        if os.path.isdir("C:/Users/parth/Desktop/Codes/Python-practice-programs/docx"):
            move(i, "C:/Users/parth/Desktop/Codes/Python-practice-programs/docx")
        else:
            os.mkdir("C:/Users/parth/Desktop/Codes/Python-practice-programs/docx")
            move(i, "C:/Users/parth/Desktop/Codes/Python-practice-programs/docx")
            
    elif i.endswith(".pptx"):
        if os.path.isdir("C:/Users/parth/Desktop/Codes/Python-practice-programs/pptx"):
            move(i, "C:/Users/parth/Desktop/Codes/Python-practice-programs/pptx")
        else:
            os.mkdir("C:/Users/parth/Desktop/Codes/Python-practice-programs/pptx")
            move(i, "C:/Users/parth/Desktop/Codes/Python-practice-programs/pptx")
            
    elif i.endswith(".bmp"):
        if os.path.isdir("C:/Users/parth/Desktop/Codes/Python-practice-programs/bmp"):
            move(i, "C:/Users/parth/Desktop/Codes/Python-practice-programs/bmp")
        else:
            os.mkdir("C:/Users/parth/Desktop/Codes/Python-practice-programs/bmp")
            move(i, "C:/Users/parth/Desktop/Codes/Python-practice-programs/bmp")
    else:
        continue
            