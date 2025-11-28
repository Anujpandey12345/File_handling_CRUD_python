from pathlib import Path
import os

def ReadFileandFolder():
    path = Path('') # Empty space gives you path of Current Directry and Folder...
    items = list(path.rglob('*')) # ecursive GLoble function read all the Item's Recursively 
    for i, items in  enumerate(items):
        print(f"{i+1} : {items} ")


def createfile():
    try:
        ReadFileandFolder()
        name = input("Please tell your file name :- ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("What you want to write in this file :- ")
                fs.write(data)
            print(f"FILE CREATED SUCCESSFULLY")
        else:
            print("This file already exist")
    except Exception as err:
        print(f"An error occured as {err}")


def readfile():
    try:
        ReadFileandFolder()
        name = input("Which file you want to read :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)
            print("Readed successfully")
        else:
            print("The file doesn't exist")


    except Exception as err:
        print(f"An error occured as {err} ")



def updatefile():
    try:

        ReadFileandFolder()
        name = input("tell me which file you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your file")
            print("Press 2 for overwriting the data of your file")
            print("Press 3 for appending some content in your file")


            res = int(input("tell your response :- "))
            if res == 1:
                name2 = input("tell your new file name :- ")
                p2 = Path(name2)
                p.rename(p2)


            if res == 2:
                with open(p, "w") as fs:
                    data = input("tell what you want to write this will overwrite the data on your file :- ")
                    fs.write(data)

            if res == 3:
                with open(p, "a") as fs:
                    data = input("tell what you want to append")
                    fs.write(" "+data)
    except Exception as err:
        print(f"An error occured as {err} ")



def deletefile():
    try:

        ReadFileandFolder()
        name = input("tell me which file you want to delete :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("File removed successfully")
        else:
            print("No such file Exist")
    except Exception as err:
        print(f"An error occured as {err} ")

        


print("Press 1 for Creating a file :- ")
print("Press 2 for Reading a file :- ")
print("Press 3 for Updating a file :- ")
print("Press 4 for Deleting a file :- ")

check = int(input("Please tell your response :- "))

if check ==  1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()


if check == 4:
    deletefile()

