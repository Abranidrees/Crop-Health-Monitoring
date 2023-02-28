
# Crop-Health-Monitoring
## Introduction
The increased demand for food due to rapid population growth has been identified as a global concern that calls for innovative approaches to achieve sustainable agriculture (FAO, 2017). Remote sensing offers an improved, reliable and timely way of crop monitoring and planning. The spectral and multi-temporal resolutions enable the study of the rapidly changing phenological differences in a cost-effective way. Using satellite imagery and vegetation indices (the arithmetic combination of spectral bands that relate to vegetation) has proved to be an efficient source of reliable data for farmers to make informed decisions at different scales. Some of the globally adopted vegetation indices to monitor vegetation indices include the Normalized Difference Vegetation Index (NDVI), Enhanced Vegetation Index (EVI), and Green Chlorophyll Index (GCI).

NDVI is very popular and useful in monitoring the greenness or chlorophyll content in crops. NDVI is a ratio computed using the red band and the Near-infrared band. The values of NDVI range from 1 to -1, where 1 indicates very healthy vegetation and -1 means dead vegetation. NDVI cancels out the topography effects because of the similarities between the visible region and the Near-infrared region, however; it is prone to errors caused by canopy structural variations and plant physiognomy. Therefore, the need for EVI to compensate for that error. EVI helps to detect stress and changes because of drought and it is computed from the blue, red, and near-infrared bands with some constants. GCI is like NDVI but it uses the green reflectance of vegetation and NIR spectral bands to estimate the amount of chlorophyll present in the vegetation. This web application uses Sentinel 2 images to compute the vegetation indices.


## Objectives
The objective of this web application is to provide an easy access and friendly interface for farmers, agronomists and relevant stakeholders with reliable data at their reach to assess crop health, guide them to make informed decisions and reduce the amount for fertilizers. 
## Data and Method
This project used sentinel-2 satellite images and boundaries of a few selected study areas in polygon geojson format. Sentinel-2 is the land monitoring mission from the EU Copernicus Programme that consists of the constellation of twin satellites Sentinel-2A and 2B. They provide fine-resolution optical imageries with global coverage and a revisit time of 5 days with satellite constellation. (Earth Online European Space Agency, 2014). Sentinel 2 images have a range of spatial resolutions, but we used the bands with 10m resolutions in this project.

The backend was developed using python. The downloading and processing of images are carried out by functions in the main file. The “app.py” file is the flask application created to extract data from the database. The front end, which enables the visualization of the results was developed using HTML, CSS and JavaScript. The web map interface incorporates Leaflet, which is an open-source JavaScript library.
## Installation

First thing is to create the environment in your computer for that you have to install Miniconda, pgAdmin, and VS code.

Miniconda : https://youtu.be/oHHbsMfyNR4

pgAdmin : https://youtu.be/0n41UTkOBb0

VS Code : https://youtu.be/JPZsB_6yHVo

After installaltion you have to open the Anaconda prompt and run the line of code to create the environment.
Note: Downlaod our full folder "Crop-Health-Monitoring" and make sure you are creating the environment in our downloaded folder.
```bash
  conda create -n project
```
project is the name of the environment, then you have to activate your project with this command. 
```bash
  conda activate project
```
Then, you have to run that line of code to in all teh libaraies which we need to run that app. 
```bash
  conda install --file requirements.txt -c conda-forge
```
## Workflow
![workflow](https://user-images.githubusercontent.com/126249551/221832545-5c0ec23e-6b19-4c7c-8fbc-37b695e0f922.jpg)


## How to run the APP
Follow these steps to run the app.

1. Give the path   for two geoJSON files of  same study area one in WSG84 Coordinate system (to search the images for that area )and other in projected Coordinate system (To clip the images) according to the UTM zone for that particular place.
![Screenshot_20230227_093325](https://user-images.githubusercontent.com/126249551/221710873-44dcc57b-80de-4783-bfed-5d7df8de739f.png)
2. Check the update the ending and starting date (This app currently is not working for offline images).
![Screenshot_20230227_093431](https://user-images.githubusercontent.com/126249551/221710962-f1e7c223-e06c-4edd-804e-01c998372d4f.png)
3. Ensure you have login credentials. If not register on Sentinel Hub to get that.Copy your credentials into the required python files.
![Screenshot_20230227_093520](https://user-images.githubusercontent.com/126249551/221711286-f26d4d06-4741-4985-957a-2b30de52233a.png)
4. Update the credentials  of the database and table in the required python files (main.py and app.py)
![Screenshot_20230227_093557](https://user-images.githubusercontent.com/126249551/221711323-13981664-14ad-49a6-9718-082d6dd512d1.png)
5. Run the "main.py"


https://user-images.githubusercontent.com/126249551/221715012-e3bc0285-d61c-4dbc-bbb5-0dcc729ab074.mp4



#### Working
main.py file did these steps
1. Create the folders in your C drive to put the downloaded images, Cliped images and processed Indices.
2. Look the S2 images for your study area  according to your given time period then download the specific bands (Band-2348) instead of whole image and put them in the folder "download" (main.py will create that folder automatically)
3. Getting the specifc metadata for downloaded image and upload that data in database.
4. Clip the bands with your uploaded geoJSON files (Study area) put these clip bands in the folder "processed"(main.py will create that folder automatically)
5. Calculate the indices and put these indices in the folder "indices" (main.py will create that folder automatically)


## Database Connection
Open the db.sql file in pgAdmin 4 (Crop-Health-Monitoring/database/) and run this file.
![Screenshot_20230228_105104](https://user-images.githubusercontent.com/126249551/221832963-0b0cc2d0-9b9e-430c-bae2-bafbf1e3ca43.png)


Note: If you change the table name or database name, you have to change also in main.py
#### Working
This sql file will create the database, create the postgis extension for the database and table for the metadata of the S2 Imgaes.
## Outputs and visualization
### Outputs
The downloaded, processed bands and indices are stored on the local Disk and can be visualized using any suitable software application. The image metadata are contained in the PostgreSQL dB. The image metadata and the footprint of the images can be visualized using the web map interface.
### Visualization
Follow these steps to visualized this web map
1. Update the credentials of the database in app.py file(Crop-Health-Monitoring/App/app.py)
![Screenshot_20230227_093622](https://user-images.githubusercontent.com/126249551/221712098-6e2cc800-f5f9-48ea-8144-412d9e0df83d.png)

2. Run the app.py file and open the localhost link.



https://user-images.githubusercontent.com/126249551/221716299-a840608b-ab7c-4981-8698-b4d2ea7dfa14.mp4




#### Working
The web map interface functionalities include an attribute pop-up when clicking on the footprint polygon, a button to display attributes/metadata, and a quick URL to view the sentinel images.
## Future updates:
We will update this web app
1. Calculate the indices from multiple images
2. Displaying the indices in web app 
3. Centralized database system.
4. Multi-temporal vegetation indices analysis and comparison in web dashboard.

Web visualization of multi-temporal indices line plot.
It is pertinent to state that this app is developed for educational and research purposes. Future updates will be made if it will be suitable for commercial purposes
## Authors
1. Abran Idrees
He earned a bachelor's degree in Space Science from the university of the Punjab, Lahore, Pakistan and now he is pursuing a master's degree in Geospatial Technologies at NOVA IMS, Universidade NOVA de Lisboa, Portugal.

2. Joao Maria Telo Abreu Jardine Neto
He earned a bachelor's degree in Spatial Planning from Instituto de Geografia e Ordenamento do Território, Portugal and now he is also pursuing a master's degree in Geospatial Technologies at NOVA IMS, Universidade NOVA de Lisboa, Portugal.

3. Lukumon Olaitan Lateef
He holds a bachelor’s degree in surveying and geoinformatics from the Federal University of Technology, Akure in Nigeria and now he is also pursuing a master's degree in Geospatial Technologies at NOVA IMS, Universidade NOVA de Lisboa, Portugal.

## References
Food and Agriculture Organization of the United Nations (2017). The future of food and agriculture - Trends and challenges. Agricultural productivity and innovation (pp. 46–47), Rome: FAO. Matsushita, B., Yang, W., Chen, J., Onda, Y., & Qiu, G. (2007). Sensitivity of the Enhanced Vegetation Index (EVI) and Normalized Difference Vegetation Index (NDVI) to Topographic Effects: A Case Study in High-density Cypress Forest. Sensors, 7(11), 2636–2651. MDPI AG. Retrieved from http://dx.doi.org/10.3390/s7112636 Updates
