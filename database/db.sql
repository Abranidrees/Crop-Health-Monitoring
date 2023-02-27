-- Creates a database named "GPS_project"
CREATE DATABASE "tech"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE EXTENSION postgis; -- postgis extension for the database

-- This line creates a schema "sa" and "pa" inside the Table

CREATE SCHEMA sa; -- stagging area
CREATE SCHEMA pa; -- production area

-- This line creates a table inside schema "sa"
DROP TABLE IF EXISTS sa.image_meta;

CREATE TABLE sa.image_meta(
   id UUID PRIMARY KEY,
    title TEXT NOT NULL,
    footprint GEOMETRY(POLYGON) NOT NULL,
    date TIMESTAMP NOT NULL,
    "cloud_cover_percentage" FLOAT NOT NULL,
    "Identifier" TEXT NOT NULL,
    "processing_level" TEXT NOT NULL,
    "product_type" TEXT NOT NULL,
	"Size" TEXT NOT NULL,
    "Illumination Azimuth Angle" FLOAT NOT NULL,
    "Illumination Zenith Angle" FLOAT NOT NULL,
    "quicklook_url" TEXT NOT NULL);
	
-- to add new column in the table
ALTER TABLE sa.image_meta
ADD COLUMN Foot_print Text NULL;
-- to see the table
SELECT * FROM sa.image_meta;
