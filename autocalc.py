import arcgis
import os
import time
import math

# Optional, only use in case of particularly large bag files
import arcpy
arcpy.env.parallelProcessingFactor = "0"
# Optional, only use in case of particularly large bag files

def time_format(t): #only to tell time elapsed
    out = ""
    if t >= 3600:
        t = t / 3600 
        out+=str(math.floor(t))+" hours, "
        t-=math.floor(t)
        t = t*3600
    if t >= 60:
        t = t / 60 
        out+=str(math.floor(t))+" minutes, "
        t-=math.floor(t)
        t = t*60
    if t > 0:
        out+=str(t)+" seconds, "
    return out

'''
change project_space to the copied project folder path
'''
project_space = r"C:\Project"

bag_dir_path = os.path.join(project_space,"SRC_BAG")
folder_names = [name for name in os.listdir(bag_dir_path) if os.path.isdir(os.path.join(bag_dir_path, name))]
bag_list = []
for folder in folder_names:
    folder_dir = os.path.join(bag_dir_path, folder)
    bag_files = [file for file in os.listdir(folder_dir) if file.endswith('.bag')]
    for bag_file in bag_files:
        bag_list.append(os.path.join(folder_dir, bag_file))
        print(os.path.join(folder_dir, bag_file))


#folder creation
slope_folder = os.path.join(project_space,"SLOPE_RASTERS")
if not os.path.exists(slope_folder):
    os.mkdir(slope_folder)
else:
    print(f"Folder '{slope_folder}' already exists.")
sobel_folder = os.path.join(project_space,"SOBEL_RASTERS")
if not os.path.exists(sobel_folder):
    os.mkdir(sobel_folder)
else:
    print(f"Folder '{sobel_folder}' already exists.")


#slope
start_time = time.time()
for bag in bag_list:
    bag_layer = arcgis.raster.Raster(bag)
    result = arcgis.raster.functions.slope(bag_layer)
    out_path = os.path.join(slope_folder,(os.path.basename(bag)[:-4]+'_Slope.tif'))
    result.save(out_path)
    print(f"Saved to: {os.path.basename(os.path.dirname(bag))}")
end_time = time.time()
print(f"Time Elapsed: {time_format(end_time-start_time)}")


#sobel vertical
sobel_vertical = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]
start_time = time.time()
for bag in bag_list:    
    bag_layer = arcgis.raster.Raster(bag)
    result = arcgis.raster.functions.convolution(raster=bag_layer, kernel=sobel_vertical)
    out_path = os.path.join(sobel_folder,(os.path.basename(bag)[:-4]+'_SobVert.tif'))
    result.save(out_path)
    print(f"Saved to: {os.path.basename(os.path.dirname(bag))}")
end_time = time.time()
print(f"Time Elapsed: {time_format(end_time-start_time)}")