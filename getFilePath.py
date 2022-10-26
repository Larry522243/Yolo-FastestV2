import os

allFiles = os.listdir("./newImage/val")

for file in allFiles:
    if ".jpg" in file:
        print("./newImage/val/" + file)