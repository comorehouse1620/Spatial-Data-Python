
'''
Author: Claire Morehouse
Description: This script checks if a shapefile at a certain filepath location exists
Inputs: The string "cities.shp" into arcpy.exists
Outputs: True or false (in this case false)
'''

#import python site package
import arcpy
#set up environment/workspace
from arcpy import env
env.workspace = "C:\\Users\\CMorehouse\\Desktop\\compprog\\Lab3\\Data"
# set variable to arcpy.exists for the cities shapefile (checks in something exists))
shape_exists = arcpy.Exists("CITIES.SHP")
# print variable
print shape_exists
