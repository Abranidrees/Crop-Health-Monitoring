import os
import rasterio
import numpy as np


def process_ndvi(folder):
    
    """
     Process the normalized difference vegetation index (NDVI) for Sentinel-2 images in a folder.

    Args:
        folder (str): The path to the folder containing Sentinel-2 images.

    Returns:
        None

    Raises:
        ValueError: If the folder does not contain processed Sentinel-2 images with red and NIR bands.

    This function calculates the NDVI from the red and NIR bands of Sentinel-2 images that have been processed 
    and downloaded into the specified folder. It then writes the NDVI to a new GeoTIFF file in a subfolder called 'indices'.
    The output file name is derived from the red band file name, with '_ndvi' appended to it. The output file has the same 
    coordinate reference system (CRS) and spatial extent as the input red band file.

    Example usage:
    >>>> process_ndvi('/path/to/sentinel2_images/')
    """
    download = os.path.join(folder, 'download')
    processed = os.path.join(folder, 'processed')
    indices = os.path.join(folder, 'indices')
    # Formula to calculate the ndvi
    def calculate_ndvi(red, nir):
        ndvi = (nir - red) / (nir + red)
        return ndvi

    red_file = None
    nir_file = None

    # Find the red and NIR bands in the folder
    for filename in os.listdir(processed):
        if 'B04' in filename:
            red_file = os.path.join(processed, filename)
        elif 'B08' in filename:
            nir_file = os.path.join(processed, filename)

    with rasterio.open(red_file) as src_red:
        red = src_red.read(1).astype(np.float32) / 65535

    with rasterio.open(nir_file) as src_nir:
        nir = src_nir.read(1).astype(np.float32) / 65535

    ndvi = calculate_ndvi(red, nir)

    # Create the output folder if it doesn't exist
    if not os.path.exists(indices):
        os.makedirs(indices)

    # Write the NDVI to a new TIFF file in the output folder
    output_filename = os.path.splitext(os.path.basename(red_file))[0] + '_ndvi.tif'
    with rasterio.open(os.path.join(indices, output_filename), 'w', driver='GTiff',
                       height=ndvi.shape[0], width=ndvi.shape[1],
                       count=1, dtype=np.float32, crs=src_red.crs, transform=src_red.transform) as dst:
        dst.write(ndvi.astype(np.float32), 1)

def process_gci(folder):
    """
    Process the Green Chlorophyll Index (GCI) for Sentinel-2 imagery in the given folder.

    Parameters:
        folder (str): Path to the folder containing Sentinel-2 imagery in the SAFE format.

    Returns:
        None.

    Raises:
        FileNotFoundError: If the input folder does not exist or does not contain the required bands.

    This function reads the Green and Near-Infrared (NIR) bands from the Sentinel-2 imagery
    in the input folder, calculates the GCI using the formula (NIR / Green) - 1, and writes
    the resulting GCI to a new GeoTIFF file in a subfolder called "indices". The output
    file has the same name as the input Green band file, with "_gci.tif" appended to it.

    """
    processed = os.path.join(folder, 'processed')
    indices = os.path.join(folder, 'indices')
    # Formula to calculate the GCI
    def calculate_gci(green, nir):
        gci = (nir / green) - 1
        return gci

    green_file = None
    nir_file = None

    # Find the Green and NIR bands in the folder
    for filename in os.listdir(processed):
        if 'B03' in filename:
            green_file = os.path.join(processed, filename)
        elif 'B08' in filename:
            nir_file = os.path.join(processed, filename)

    with rasterio.open(green_file) as src_green:
        green = src_green.read(1).astype(np.float32) / 65535

    with rasterio.open(nir_file) as src_nir:
        nir = src_nir.read(1).astype(np.float32) / 65535

    gci = calculate_gci(green, nir)

    # Create the output folder if it doesn't exist
    if not os.path.exists(indices):
        os.makedirs(indices)

    # Write the GCI to a new TIFF file in the output folder
    output_filename = os.path.splitext(os.path.basename(green_file))[0] + '_gci.tif'
    with rasterio.open(os.path.join(indices, output_filename), 'w', driver='GTiff',
                       height=gci.shape[0], width=gci.shape[1],
                       count=1, dtype=np.float32, crs=src_green.crs, transform=src_green.transform) as dst:
        dst.write(gci.astype(np.float32), 1)

def process_evi(folder):
    """
    Processes Enhanced Vegetation Index (EVI) from Sentinel-2 satellite data using the red, blue and NIR bands.
    
    Args:
    folder (str): Path to the folder containing Sentinel-2 data files.
    
    Returns:
    None
    
    This function searches for the blue, red and NIR band files in the specified folder, and uses them to calculate
    the EVI. The calculated EVI is written to a new TIFF file in a subfolder named 'indices' in the same folder.
    """
    
    processed = os.path.join(folder, 'processed')
    indices = os.path.join(folder, 'indices')

    def calculate_evi(red, blue, nir, lai=2.5, gain=2.5, offset=6):
        evi = evi = gain * ((nir - red) / (nir + (lai * red) - (offset * blue) + 1))
        return evi

    blue_file = None
    red_file = None
    nir_file = None

    # Find the blue, red and NIR bands in the folder
    for filename in os.listdir(processed):
        if 'B02' in filename:
            blue_file = os.path.join(processed, filename)
        if 'B04' in filename:
            red_file = os.path.join(processed, filename)
        elif 'B08' in filename:
            nir_file = os.path.join(processed, filename)

    with rasterio.open(blue_file) as src_blue:
        blue = src_blue.read(1).astype(np.float32) / 65535

    with rasterio.open(red_file) as src_red:
        red = src_red.read(1).astype(np.float32) / 65535
    
    with rasterio.open(nir_file) as src_nir:
        nir = src_nir.read(1).astype(np.float32) / 65535

    evi = calculate_evi(red, blue, nir, lai=2.5, gain=2.5, offset=6)

    # Create the output folder if it doesn't exist
    if not os.path.exists(indices):
        os.makedirs(indices)

    # Write the EVI to a new TIFF file in the output folder
    output_filename = os.path.splitext(os.path.basename(blue_file))[0] + '_evi.tif'
    with rasterio.open(os.path.join(indices, output_filename), 'w', driver='GTiff',
                       height=evi.shape[0], width=evi.shape[1],
                       count=1, dtype=np.float32, crs=src_red.crs, transform=src_red.transform) as dst:
        dst.write(evi.astype(np.float32), 1)    

   
