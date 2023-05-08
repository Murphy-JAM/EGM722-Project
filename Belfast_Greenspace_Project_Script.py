# import packages
import geopandas as gpd
import cartopy
import notebook
import rasterio as rio
import pyepsg
import folium
import os

# open data files
parks = gpd.read_file('C:\\Users\\Julie\\Desktop\\Documents\\PostGrad\\Python Assess\\Project\\Greenspace_Python_Project_Data\\Belfast_Parks.shp')
residential_properties = gpd.read_file('C:\\Users\\Julie\\Desktop\\Documents\\PostGrad\\Python Assess\\Project\\Greenspace_Python_Project_Data\\Belfast_Pointer.shp')
small_areas = gpd.read_file('C:\\Users\\Julie\\Desktop\\Documents\\PostGrad\\Python Assess\\Project\\Greenspace_Python_Project_Data\\Belfast_Small_Areas.shp')
