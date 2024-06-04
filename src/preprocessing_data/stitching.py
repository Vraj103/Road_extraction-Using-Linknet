# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 23:58:32 2024

@author: LENOVO
"""

import cv2
import numpy as np

# Read the original image to get its dimensions
img_path = "D:/S2A_MSIL2A_20230414T161831_N0509_R040_T17TNJ_20230415T001100.SAFE/GRANULE/L2A_T17TNJ_A040792_20230414T162739/IMG_DATA/R10m/TIFF's from arcgis/T17TNJ_20230414T161831_TCI_10m.tif"
img = cv2.imread(img_path)
rows, cols, _ = img.shape
print(f"Original image dimensions: {img.shape}")

# Define the tile size
tile_size = (256, 256)

# Create an empty image of the same size as the original
stitched_img = np.zeros((rows, cols, 3), dtype=np.uint8)

# Loop over the tiles and place them back into the empty image
for i in range(0, rows, tile_size[1]):
    for j in range(0, cols, tile_size[0]):
        # Construct the filename of the current tile
        tile_filename = f"debug_{i//tile_size[1]}_{j//tile_size[0]}.tif"
        
        # Read the current tile
        tile = cv2.imread(tile_filename)
        
        if tile is not None:
            # Calculate the boundaries of the current tile
            y_start = i
            y_end = min(i + tile_size[1], rows)
            x_start = j
            x_end = min(j + tile_size[0], cols)
            
            # Place the tile back into the empty image
            stitched_img[y_start:y_end, x_start:x_end] = tile
        else:
            print(f"Tile {tile_filename} not found")

# Save the stitched image
cv2.imwrite("stitched_image.tif", stitched_img)

# Optionally, display the stitched image
# cv2.imshow("Stitched Image", stitched_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()