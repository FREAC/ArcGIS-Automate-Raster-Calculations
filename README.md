## ArcGIS-Automate-Raster-Calculations
Automated raster calculations on .bag files using arcpy functions 

# Scipt features:

-Automates esri-based raster calculations on .bag files, but can be altered to include any raster format. 

-Stores Slope and Sobel Vertical convolutions of all rasters in their own folders
 
# How to use this script:

1. Save or copy this code to a python IDE (jupyter notebook, ArcGIS Python window)

2. Copy the folder of the ArcGIS project as a path

3. Change the project_space variable to the directory name, using either \\ or / (not single \)

4. Make sure the "SRC_BAG" in the bag_dir_path variable matches the name of the folder where original .bag files are stored

5. Run code if only needing Slope and Sobel Vertical convolutions

6. After completion, the new rasters will be stored as .tifs in their respective SLOPE_RASTERS and SOBEL_RASTERS folders.
