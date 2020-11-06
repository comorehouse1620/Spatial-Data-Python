'''
Author: Claire Morehouse
Description: This script prints the fields for a particular shapefile
Inputs: Cities shapefile
Outputs: Printed name of fields and the variable type
'''

# import arcpy package
import arcpy
# set up environment/workspace
from arcpy import env
env.overwriteOutput = True
env.workspace = "C:\\Users\\CMorehouse\\Desktop\\compprog\\Lab3\\Data"
#set variable equal to listfields arcpy 
fieldlist = arcpy.ListFields("cities.shp")
# create for loop that prints element of the fieldlist variable 
for field in fieldlist:
    print field.name + " " + field.type

'''
Output from run:
FID OID
Shape Geometry
CITIESX020 Double
FEATURE String
NAME String
POP_RANGE String
POP_2000 Integer
FIPS55 String
COUNTY String
FIPS String
STATE String
STATE_FIPS String
DISPLAY SmallInteger
'''
