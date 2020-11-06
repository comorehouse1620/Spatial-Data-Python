'''
Author: Claire Morehouse
Description: This script imports the package arcpy, sets up a work environment
and then sets a variable equal to the list of feature classes in the work environment.
A for loop then describes each object in the workspaces
Inputs: feature classes in the workspace
Outputs: a description of the feature classes (name + data type)
'''
# import arcpy package
import arcpy
#set up workspace/environment
from arcpy import env
env.workspace = "C:\\Users\\CMorehouse\\Desktop\\compprog\\Lab3\\Data"
# define variable equal to feature class list
fclist = arcpy.ListFeatureClasses()
# set up for loop to describe each variable
for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    print "Name: " + fcdescribe.name
    print "Data type: " + fcdescribe.dataType
'''
Output for above:
Name: amtrak_stations.shp
Data type: ShapeFile
Name: cities.shp
Data type: ShapeFile
Name: counties.shp
Data type: ShapeFile
Name: new_mexico.shp
Data type: ShapeFile
Name: railroads.shp
Data type: ShapeFile
'''

