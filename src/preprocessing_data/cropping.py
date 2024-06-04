# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2

# Read the image from the specified path
img = cv2.imread("D:/S2A_MSIL2A_20230414T161831_N0509_R040_T17TNJ_20230415T001100.SAFE/GRANULE/L2A_T17TNJ_A040792_20230414T162739/IMG_DATA/R10m/TIFF's from arcgis/T17TNJ_20230414T161831_TCI_10m.tif")

# Get the dimensions of the image
rows, cols, _ = img.shape
print(f"Image dimensions: {img.shape}")

# Define the tile size
tile_size = (256, 256)

# Loop over the image and extract tiles
for i in range(0, rows, tile_size[1]):
    for j in range(0, cols, tile_size[0]):
        # Calculate the boundaries of the current tile
        y_start = i
        y_end = min(i + tile_size[1], rows)
        x_start = j
        x_end = min(j + tile_size[0], cols)
        
        # Extract the current tile
        cropped_img = img[y_start:y_end, x_start:x_end]
        
        # Save the current tile for debugging
        cv2.imwrite(f"debug_{i//tile_size[1]}_{j//tile_size[0]}.tif", cropped_img)

        # Optionally, display the current tile (uncomment the next two lines if needed)
        # cv2.imshow(f"Tile {i//tile_size[1]},{j//tile_size[0]}", cropped_img)
        # cv2.waitKey(0)

# Close all OpenCV windows (uncomment if you use imshow and waitKey)
# cv2.destroyAllWindows()
