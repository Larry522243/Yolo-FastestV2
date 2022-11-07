import os

files = os.listdir("./valid/images")
names = []

for file in files:
    names.append(file[: -4])

print(names)

n = 0
for name in names:
    os.rename("./valid/images/" + name + ".jpg", "./valid/images/" + str(n).zfill(5) + ".jpg")
    os.rename("./valid/labels/" + name + ".txt", "./valid/labels/" + str(n).zfill(5) + ".txt")
    n += 1