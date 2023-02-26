# Importing Libaraies
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt, make_path_filter
import pandas as pd
import requests
import json

def download_sentinel2_data(footprint, date_range, cloudcoverpercentage, api, download_path):
    """
    Downloads Sentinel-2 Level-2A imagery for a given footprint and time range, with specified cloud cover percentage.

    Args:
    - footprint (str): geojson format of the area of interest.
    - date_range (str): Start and end date in the format 'yyyy-mm-dd /yyyy-mm-dd'.
    - cloudcoverpercentage (tuple): Tuple of minimum and maximum cloud cover percentage.
    - api (sentinelhub.SentinelHub): Instance of the Sentinel Hub API.
    - download_path (str): Local directory path to download the imagery.

    Returns:
    - product_id (str): Unique identifier of the downloaded product.

    Raises:
    - Exception: If no image is available under given specification, an exception is raised.

    """
    try:
        products = api.query(footprint,
                         date=date_range,
                         platformname='Sentinel-2',
                         processinglevel='Level-2A',
                         cloudcoverpercentage=cloudcoverpercentage,
                     )
        products_gdf = api.to_geodataframe(products)
        products_gdf_sorted = products_gdf.sort_values(['cloudcoverpercentage'], ascending=[True])
    except:
        print("No image is available under given specification, kindly check the date period or cloud coverage")

    df = pd.DataFrame(products_gdf_sorted, columns= ['title', 'link', 'uuid'])
    result = df.iloc[1,2]
    product_id = str(result)
    
    path_filter = make_path_filter("*_B0[2348]_10m.jp2")
    print("Start Downloading Bands")
    api.download(product_id, download_path, nodefilter=path_filter)
    print("Downloaded Bands")
    return product_id
