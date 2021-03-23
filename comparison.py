#this is my first attempt to use def functions, so wish me luck (:



import numpy as np
from numpy import loadtxt
import re
import os.path
from os import path


R17 = []
R18 = []
R19 = []
R20 = []
R1 = []
R2 = []
R3 = []
R4 = []
R5 = []
R6 = []
R7 = []
R8 = []

unique_gf = []

GeneFamilies = 47000

for i in range (1, GeneFamilies+1):
        file = path.exists('R17_BL-Miss/bmge_files.5/%i.bmge' %i)
        #print("file exist?" + str(file)+ str(i))
        if file is True:
                R17.append(i)
                #print( str(i)+ ".bmge")

for i in range (1, GeneFamilies+1):
        file = path.exists('R18_BL-Miss/bmge_files.5/%i.bmge' %i)
        if file is True:
                R18.append(i)

for i in range (1, GeneFamilies+1):
        file = path.exists('R19_BL-Miss/bmge_files.5/%i.bmge' %i)
        if file is True:
                R19.append(i)

for i in range (1, GeneFamilies+1):
        file = path.exists('R20_BL-Miss/bmge_files.5/%i.bmge' %i)
        if file is True:
                R20.append(i)

for i in range (1, GeneFamilies+1):
        file = path.exists('R1_BL-Miss/bmge_files.5/%i.bmge' %i)
        if file is True:
                R1.append(i)

for i in range (1, GeneFamilies+1):
        file = path.exists('R2_BL-Miss/bmge_files.5/%i.bmge' %i)
        if file is True:
                R2.append(i)

for i in range (1, GeneFamilies+1):
        file = path.exists('R3_BL-Miss/bmge_files.5/%i.bmge' %i)
        if file is True:
                R3.append(i)

for i in range (1, GeneFamilies+1):
        file = path.exists('R4_BL-Miss/bmge_files.5/%i.bmge' %i)
        if file is True:
                R4.append(i)

for i in range (1, GeneFamilies+1):
        file = path.exists('R5_BL-Miss/bmge_files.5/%i.bmge' %i)
        if file is True:
                R5.append(i)

for i in range (1, GeneFamilies+1):
        file = path.exists('R6_BL-Miss/bmge_files.5/%i.bmge' %i)
        if file is True:
                R6.append(i)

for i in range (1, GeneFamilies+1):
        file = path.exists('R7_BL-Miss/bmge_files.5/%i.bmge' %i)
        if file is True:
                R7.append(i)

for i in range (1, GeneFamilies+1):
        file = path.exists('R8_BL-Miss/bmge_files.5/%i.bmge' %i)
        if file is True:
                R8.append(i)

def compare (x,y)
    holder = list(set(x).intersection(set(y)))
    print(holder)
    print(len(holder))

compare (R17,R18)
compare (R19,holder)
compare (R20,holder)
compare (R1,holder)
compare (R2,holder)
compare (R3,holder)
compare (R4,holder)
compare (R5,holder)
compare (R6,holder)
compare (R7,holder)
compare (R8,holder)
