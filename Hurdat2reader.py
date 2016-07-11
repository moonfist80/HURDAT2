import os
import sys
import string

data = open('hurdat2.txt','r+')
hurdat = data.readlines()

HurdatClean = open('hurdat2_clean.txt','w') #This will be the final file
##print(hurdat.readline())
##print(hurdat)

s = 'A'

for line in hurdat:
    if s in line[0]:
        Hurr_name = line.rstrip('\n')
    else:
        Hurdat_Final = Hurr_name + line
        HurdatClean.write(Hurdat_Final)
#print(HurdatClean.readline())

data.close()
HurdatClean.close()
