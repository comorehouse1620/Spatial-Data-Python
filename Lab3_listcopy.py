'''
Author: Claire Morehouse
Description: This script imports the package arcpy, and then sets up a workspace with a particular folder of data.
Then, the script creates an empty geodatabase. A variable is set equal to a list of feature classes in the data folder.
Using a for loop, for every feature in the list, those features are copied to the empty geodatabase using the basename property."
Inputs: Original shapefile data in the data folder
Outputs: A new geodatabase containing features with their baseline property as their name
'''

# import arcpy package
import arcpy
# set up workspace/environment
from arcpy import env
env.overwriteOutput = True 
env.workspace = "C:\\Users\\CMorehouse\\Desktop\\compprog\\Lab3\\Data"
# Create empty gdb
arcpy.CreateFileGDB_management("C:\\Users\\CMorehouse\\Desktop\\compprog\\Lab3\\Data\\Results", "NM.gdb")
# create variable equal to feature class list
fclist = arcpy.ListFeatureClasses()
# create for loop that copies features to new database using basename property name of the feature class 
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, "C:\\Users\\CMorehouse\\Desktop\\compprog\\Lab3\\Data\\Results\\NM.gdb\\", fcdesc.basename)
    
