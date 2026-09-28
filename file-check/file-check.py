import os

file = input("Enter filename: ")

if os.path.isfile(file):
    print("File exists.")
else:
    print("File does not exist.")
