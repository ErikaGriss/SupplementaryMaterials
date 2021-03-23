#This scripts print the file name, tree name, number of copies and makes a list (and file)
#of the name of the .bmge file
#See same script in R17 folder to see the complete explanation

import numpy as np
from numpy import loadtxt
import re

Gene_Families = 100
Name_of_file = []
data = {}

for i in range(1, Gene_Families+1):
    with open ("Trial%i.uml_rec" % i,"r") as f:
        tree = (f.readlines()[5])
        split = tree.split()
        parts = (split[3])
        split = re.split(r'[.]', parts)
        result_tree = str(split[0]+'.'+split[1])
        #print(result_tree)
    with open ("Trial%i.uml_rec" % i,"r") as f:
        copies = (f.readlines()[308])
        parts = copies.split()
        result_copies = float(parts[6])
        #print(result_copies)
    if result_copies > 0 :
        Data = { result_tree : result_copies}
        Name_of_file.append(i)
        data.update(Data)
        #print(Data)
print(data)
#print(Name_of_file)






target_files = []
for key in data.keys():
    target_files.append(key)
print(target_files)

import shutil, os
for file in target_files :
    shutil.copy(file, 'Untitled Folder')


import csv

w = csv.writer(open("output5.csv", "w"))
for key, val in data.items():
    w.writerow([key, val])
