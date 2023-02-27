# Crop-Health-Monitoring
## Introduction

The increased demand for food due to rapid population growth has been identified as a global concern that calls for innovative approaches to achieve sustainable agriculture (FAO, 2017). Remote sensing offers an improved, reliable and timely way of crop monitoring and planning. The spectral and multi-temporal resolutions enable the study of the rapidly changing phenological differences in a cost-effective way. Using satellite imagery and vegetation indices (the arithmetic combination of spectral bands that relate to vegetation) has proved to be an efficient source of reliable data for farmers to make informed decisions at different scales. Some of the globally adopted vegetation indices to monitor vegetation indices include the Normalized Difference Vegetation Index (NDVI), Enhanced Vegetation Index (EVI), and Green Chlorophyll Index (GCI).

NDVI is very popular and useful in monitoring the greenness or chlorophyll content in crops. NDVI is a ratio computed using the red band and the Near-infrared band. The values of NDVI range from 1 to -1, where 1 indicates very healthy vegetation and -1 means dead vegetation. NDVI cancels out the topography effects because of the similarities between the visible region and the Near-infrared region, however; it is prone to errors caused by canopy structural variations and plant physiognomy. Therefore, the need for EVI to compensate for that error. EVI helps to detect stress and changes because of drought and it is computed from the blue, red, and near-infrared bands with some constants. GCI is like NDVI but it uses the green reflectance of vegetation and NIR spectral bands to estimate the amount of chlorophyll present in the vegetation.
This web application uses Sentinel 2 images to compute the vegetation indices.

## Objectives

The objective of this web application is to provide an easy access and friendly interface for farmers, agronomists and relevant stakeholders with reliable data at their reach to assess crop health and guide them to make informed decisions.

## Data and Method

This project used sentinel-2 satellite images and boundaries of a few selected study areas in polygon geojson format. Sentinel-2 is the land monitoring mission from the EU Copernicus Programme that consists of the constellation of twin satellites Sentinel-2A and 2B. They provide fine-resolution optical imageries with global coverage and a revisit time of 5 days with satellite constellation. (Earth Online European Space Agency, 2014). Sentinel 2 images have a range of spatial resolutions, but we used the bands with 10m resolutions in this project. 

The backend was developed using python. The downloading and processing of images are carried out by functions in the main file. The “app.py” file is the flask application created to extract data from the database. The front end, which enables the visualization of the results was developed using HTML and JavaScript. The web map interface incorporates Leaflet, which is an open-source JavaScript library.

## How to run the APP
First thing is to create the environment in your computer for that you have to install Miniconda, pgAdmin, and VS code. After installaltion you have to run the line of code in Anaconda prompt.

The libraries/packages required to run the app are contained in “requirements.txt”.  

1.	Clone the repository to your computer
2.	Install the required libraries, preferably using the Conda forge channel
3.	Ensure you have login credentials. If not register on Sentinel Hub to get that.
4.	Copy your credentials into the required python files.
5.	Use the “db.sql” command in “Crop-Health-Monitoring/database/” to create and set up a PostgreSQL database and update the credentials in the required python files.
6.	Run the “main.py” 
7.	Run the "app.py" file using the python command
8.	Hold the “Ctrl” key on your keyboard and click the link to open the visualization interface in your web browser.

## Output and visualization

The downloaded and processed images are stored on the local Disk and can be visualized using any suitable software application. The image metadata are contained in the PostgreSQL dB. The image metadata and the study area extent can be visualized using the web map interface developed using the Leaflet. The web map interface functionalities include an attribute pop-up when clicking on the study area polygon, a button to display attributes/metadata, and a quick URL to view the sentinel images. 
## Future updates:
1.	Centralized database system.
2.	Multi-temporal vegetation indices analysis and comparison.
3.	Web visualization of multi-temporal indices line plot. 

It is pertinent to state that this app is developed for educational and research purposes. Future updates will be made if it will be suitable for commercial purposes.

## Authors

If you have any questions or feedback, please contact us. Thank you for using our web app!


## References
Food and Agriculture Organization of the United Nations (2017). The future of food and agriculture - Trends and challenges. Agricultural productivity and innovation (pp. 46–47), Rome: FAO.
Matsushita, B., Yang, W., Chen, J., Onda, Y., & Qiu, G. (2007). Sensitivity of the Enhanced Vegetation Index (EVI) and Normalized Difference Vegetation Index (NDVI) to Topographic Effects: A Case Study in High-density Cypress Forest. Sensors, 7(11), 2636–2651. MDPI AG. Retrieved from http://dx.doi.org/10.3390/s7112636
Updates
