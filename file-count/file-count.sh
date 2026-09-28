#!/bin/bash

echo "Enter directory:"
read dir

count=$(find "$dir" -maxdepth 1 -type f | wc -l)

echo "Number of files: $count"
