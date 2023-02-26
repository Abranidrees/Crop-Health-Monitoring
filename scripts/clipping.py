import rasterio
from rasterio.mask import mask
import geopandas as gp
import os

def clip_raster(raster_path, shapefile_path, output_path):
    """
        Clip a raster to the extent of a shapefile.

        This function takes a raster file (raster_path) and a shapefile (shapefile_path) as input,
        clips the raster to the extent of the shapefile, and writes the output to a new file
        specified by output_path. The output raster will have the same resolution, projection,
        and data type as the input raster.

    Parameters:
        raster_path (str): The file path to the input raster.
        shapefile_path (str): The file path to the shapefile that will be used to clip the raster.
        output_path (str): The file path to the output clipped raster.

    Returns:
        None
            """
    # Read the shapefile using geopandas
    shapes = gp.read_file(shapefile_path)

    # Read the raster using rasterio
    with rasterio.open(raster_path) as src:
        # Get the transform and bounding box of the raster
        transform = src.transform
        bbox = src.bounds

        # Clip the raster using the bounding box of the shapefile
        out_image, out_transform = rasterio.mask.mask(src, shapes.geometry, crop=True)
        out_meta = src.meta.copy()

        # Update the metadata of the output raster
        out_meta.update({
            "driver": "GTiff",
            "height": out_image.shape[1],
            "width": out_image.shape[2],
            "transform": out_transform,
        })

        # Write the output raster
        with rasterio.open(output_path, "w", **out_meta) as dest:
            dest.write(out_image)

def clip_all_bands(bands_path_list, shapefile_path, output_folder):
    """
        Clip multiple bands to the extent of a shapefile.

        This function takes a list of band files (bands_path_list) and a shapefile (shapefile_path) as input,
        clips all the bands to the extent of the shapefile, and writes the outputs to a new folder
        specified by output_folder. The output rasters will have the same resolution, projection,
        and data type as the input rasters. If the output folder does not exist, the function will create it.

        If the output file already exists, it will be overwritten.

    Parameters:
        bands_path_list (List[str]): A list of file paths to the input bands.
        shapefile_path (str): The file path to the shapefile that will be used to clip the bands.
        output_folder (str): The folder path to store the output clipped bands.

    Returns:
        None
            """

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for band_path in bands_path_list:
        band_name = band_path.split("\\")[-1].replace(".jp2", ".tif")
        output_path = f"{output_folder}/{band_name}"
        if os.path.exists(output_path):
            os.remove(output_path)
        clip_raster(band_path, shapefile_path, output_path)
    
