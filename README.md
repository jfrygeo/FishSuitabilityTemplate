# Fish Suitability Template
The fish suitability template contains a solution which could be used as a template to download new data from MODIS and update an image service with this new data. 

There are multiple parts of this template:
<li> 1. Process-MODIS-Data-py - A python script that downloads new data from [NASA MODIS](https://modis.gsfc.nasa.gov/about) and adds the data to a mosaic dataset.</li>.
<li> 2. Fish Suitability.rft - A raster function template that sits on top of the Mosaic Dataset which does the mathematics of creating fish suitability.
<li> 3. Fish Suitability.mxd - An ArcMap document which contains sample data.


## MODIS
Moderate Resolution Imaging Spectroradiometer (MODIS) is an instrument aboard the Terra and Aqua satellites and acquires imagery in 36 spectral bands for analysis in global dynamics. For more information, please visit [NASA MODIS](https://modis.gsfc.nasa.gov/about/).

## Script
The script links to two data sources - 1.Sea Surface Temperature 2. Chlorophyll. These data can be combined to run analysis such as fish suitability. 

The script downloads from:

<b> Data Access </b> http://coastwatch.pfeg.noaa.gov/erddap/files/


