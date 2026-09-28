#!/bin/bash

echo "Enter filename:"
read file

if [ -f "$file" ]; then
    cp "$file" "$file.bak"
    echo "Backup created: $file.bak"
else
    echo "File does not exist."
fi
