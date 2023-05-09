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








