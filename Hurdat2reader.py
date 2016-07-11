'''
Convert the HURDAT2 data set from the raw format to a format SQL can read.  

See HURDAT2 documentation at www.aoml.noaa.gov/hrd/hurdat for Header Row descriptions



'''


import os
import sys
import string



data = open('hurdat2.txt','r+')
HurdatClean = open('hurdat2_clean.txt','w') #This will be the final file

HeaderRow = ['StormID','StormName','RecordCount','Date','TimeUTC','RecordType',
             'HU_Status','Latitude','Longitude','MaxSusWind',
             'MinPressure','34kt_windrad_NE','34kt_windrad_SE',
             '34kt_windrad_SW','34kt_windrad_NW','50kt_windrad_NE',
             '50kt_windrad_SE','50kt_windrad_SW','50kt_windrad_NW',
             '64kt_windrad_NE','64kt_windrad_SE','64kt_windrad_SW','64kt_windrad_NW']

for item in HeaderRow:
    HurdatClean.write(item+', ')

HurdatClean.write('\n')

hurdat_raw = data.readlines()

NamedRow = 'A'

for line in hurdat_raw:
    if NamedRow in line[0]:
        Hurr_name = line.rstrip('\n')
    else:
        Hurdat_Final = Hurr_name + line
        HurdatClean.write(Hurdat_Final)

data.close()
HurdatClean.close()
