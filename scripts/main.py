# Importing Libraries
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
import geopandas as gp
from glob import glob
# importing funcrions
from config import folder, download, processed, indices
from downloading import *
from clipping import clip_all_bands
from indices import *
from db import insert_data


#Study area in geojson file for search Images
footprint = geojson_to_wkt(read_geojson(r'C:/Data/Files/Data_search_WGS84/MADRID_WGS84.geojson'))
#Study area in geojson file for clip in projected Coordinate system
shapefile = 'C:/Data/Files/Data_clip/MADRID_UTM_Z30N.geojson'
# serach the time duration of the image
date_range = ('20220901','20221130')
# cloud coverage 
cloudcoverpercentage=(0, 10)
# Copernicous api
api = SentinelAPI('abranidrees', '!@#$%^&*()', 'https://apihub.copernicus.eu/apihub', show_progressbars=True)

# Directories paths
folder_path = "c:\Data"
download_path = "C:\Data\download/"
processed_path = "C:\Data\processed/"
indices_path = "C:\Data\indices/"


# Calling function to create directories
folder(folder_path)
download(download_path)
processed(processed_path)
indices(indices_path)


################# Calling function to download the S2 bands ###############
idi = download_sentinel2_data(footprint, date_range, cloudcoverpercentage, api, download_path)

#################### Calling the S2 metadata of the product #############

metadata = api.get_product_odata(idi, full=True)


# Extract the desired attributes from the metadata dictionary
attrs = ['id', 'title', 'footprint', 'date', 'Cloud cover percentage', 'Identifier', 
         'Processing level', 'Product type', 'Size', 'Illumination Azimuth Angle', 'Illumination Zenith Angle', 'quicklook_url']
data = {attr: metadata[attr] for attr in attrs}
# Changing the keys from the dictionary due to deal with some errors in frontend
data['cloud_cover_percentage'] = data.pop('Cloud cover percentage')
data['processing_level'] = data.pop('Processing level')
data['product_type'] = data.pop('Product type')
# Getting the value of the title to whenever new image will download it will to to that folder which have the same name as title
title_value = data['title']

# Convert data to a dataframe
df = pd.DataFrame([data])

# Insert the metadata into the database
#df = meta_df
table_name = 'image_meta'
db_uri = "postgresql://postgres:postgres@localhost:5432/tech"
insert_data(df, table_name, db_uri)

################ Calling function to clip the S2 Bands##################
def get_band_names(download_folder):
    return glob(f"{download_folder}/**/*.jp2", recursive = True)

def read_shapefile(shapefile_path):
    return gp.read_file(shapefile_path, driver='GeoJSON')

bandNames = get_band_names(f"{download_path}{title_value}.SAFE")
bands_path_list = bandNames
print(bands_path_list)
shapes = read_shapefile(shapefile)
shapes.to_file("temp_shapefile.shp", driver='ESRI Shapefile')

shapefile_path = "temp_shapefile.shp"
output_folder = processed_path
clip_all_bands(bands_path_list,shapefile_path,output_folder)
print("Bands are cliped")

######################### Indices Calculation #######################
parent_folder = folder_path
process_ndvi(parent_folder)
process_gci(parent_folder)
process_evi(parent_folder)



 