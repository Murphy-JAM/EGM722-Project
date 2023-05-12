# Import project packages
import geopandas as gpd
import folium
import pandas as pd

# Open the small area shapefile using geopandas
# Preview the data by showing the first 5 rows of the dataframe
smallareas = gpd.read_file('C:\\Users\\Julie\\Desktop\\Documents\\PostGrad\\Python Assess\\Project\\New_Data_Project\\Belfast_SmallAreas.shp')
smallareas.head(5)

# Visualise the data using the hectare values of the small areas
# Set a colour ramp for these values e.g. viridis
m = smallareas.explore('Hectares', cmap='viridis')

# Read the Belfast City parks CSV file using pandas
df = pd.read_csv('C:\\Users\\Julie\\Desktop\\Documents\\PostGrad\\Python Assess\\Project\\New_Data_Project\\Belfast_Parks.csv')

# Create a geodataframe for the parks CSV file using the name, address and postcode column information.
# Set the geometry using XY point information
# Set the coordinate reference system using an EPSG WGS84 code
parks = gpd.GeoDataFrame(df[['NAME', 'ADDRESS', 'POSTCODE']], geometry=gpd.points_from_xy(df['LONGITUDE'], df['LATITUDE']), crs='epsg:4326')

# Preview the parks data by showing the first five rows of the geodataframe
parks.head(5)

# Add the Belfast City park points to the map
# Add markers and set the point marker type
# Add information popups for the park markers
# Do not include a legend for park points layer
parks.explore('NAME', m=m, marker_type='marker', popup=True, legend=False)

# Load the deprivation scores for each small area in Belfast City Council area using pandas
# Preview the deprivation data by showing the first five rows of the geodataframe
MDM = pd.read_csv('C:\\Users\\Julie\\Desktop\\Documents\\PostGrad\\Python Assess\\Project\\New_Data_Project\\MDM_2017_SA.csv')
MDM.head(5)

# Join the deprivation scores to Belfast City small areas based on a shared table attribute e.g. SA2011
merged = smallareas.merge(MDM, left_on='SA2011', right_on='SA2011')

# Create a map that illustrates deprivation scores for each small area and the locations of Belfast City parks
# Display the deprivation values as the scale
# Use the Red/Yellow/Green colourmap to show the deprivation scale
# Set the map legend
# Add markers and set the point marker type
# Add information popups for the park markers
# Do not include a legend for the park points layer
# Make the markers dark green with a tree icon
m = merged.explore('MDM_Rk1wt', cmap='RdYlGn', legend_kwds={'caption': 'Deprivation Measure - least affluent (1) to most affluent (4537)'})
parks_args = {'m': m, 'marker_type': 'marker', 'popup': True, 'legend': False, 'marker_kwds': {'icon': folium.Icon(colour='darkgreen', icon='tree', prefix='fa')}}

# Use the parks_args with the ** unpacking operator (for dictionaries)
parks.explore('NAME', **parks_args)

# Show the final map
m

# Save map as an html file
m.save('Belfast_Greenspace_VS_Deprivation.html')
