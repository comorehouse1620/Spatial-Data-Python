'''
Author: Claire Morehouse
Description: This script describes data with the describe function and check its properties 
Inputs: Shapefile/layer
Output: Properties of the shapefile/layer
'''

# Run myshape equal to describe which allows access to properties of an object
myshape = arcpy.Describe("C:\\Users\\CMorehouse\\Desktop\\compprog\\Lab3\\Data\\cities.shp")

#Check properties 
myshape.dataType
# Output: u'Shapefile'

# Run my layer equal to describe which allows access to properties of an object 
# File is now being accessed from within ArcMap instead of the file path (above)
mylayer = arcpy.Describe("cities")
mylayer.dataType
# Output: U'FeatureLayer'

mylayer.datasetType
#Output: u'FeatureClass'

mylayer.catalogPath
# Output: u'C:\\Users\\CMorehouse\\Desktop\\compprog\\Lab3\\Data\\cities.shp'

mylayer.basename
# Output: u'cities'

mylayer.file
# Output: u'cities.shp'

mylayer.isVersioned
# Output: False

mylayer.shapeType
# Output: u'Point'

mylayer.spatialReference
# Output: <geoprocessing spatial reference object object at 0x13FAAD10>

mylayer.spatialReference.name
# Output: u'GCS_North_American_1983'

mylayer.spatialReference.type
# Output: u'Geographic'

mylayer.spatialReference.domain
# Output
u'-400 -400 400 400'
