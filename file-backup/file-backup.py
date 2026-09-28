import os
import shutil

file = input("Enter filename: ")

if os.path.isfile(file):
    backup = file + ".bak"
    shutil.copy(file, backup)
    print(f"Backup created: {backup}")
else:
    print("File does not exist.")
