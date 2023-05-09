# import packages
import geopandas as gpd
import cartopy
import notebook
import rasterio as rio
import pyepsg
import folium
import os
import pandas as pd

# open small area file and preview data
smallareas = gpd.read_file('C:\\Users\\Julie\\Desktop\\Documents\\PostGrad\\Python Assess\\Project\\New_Data_Project\\Belfast_SmallAreas.shp')
smallareas.head(5)

# use the small areas size (ha) to visualise the polygons and set colour scheme
m = smallareas.explore('Hectares', cmap='viridis')

# read the Belfast parks csv file
df = pd.read_csv('C:\\Users\\Julie\\Desktop\\Documents\\PostGrad\\Python Assess\\Project\\New_Data_Project\\Belfast_Parks.csv')

# create a new geodataframe using the name, address and postcode columns of the csv file.
# set the geometry using points from xy
# set the coordinate reference system using WGS84 code
parks = gpd.GeoDataFrame(df[['NAME','ADDRESS','POSTCODE']], geometry=gpd.points_from_xy(df['LONGITUDE'], df['LATITUDE']), crs='epsg:4326')









