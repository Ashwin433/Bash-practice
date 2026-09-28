import os

directory = input("Enter directory: ")

count = 0

for item in os.listdir(directory):
    path = os.path.join(directory, item)

    if os.path.isfile(path):
        count += 1

print("Number of files:", count)
