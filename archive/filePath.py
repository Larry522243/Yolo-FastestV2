import os

files = os.listdir("./val")

for file in files:
    if ".jpg" in file:
        print("archive/val/" + file)