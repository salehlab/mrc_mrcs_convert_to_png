import mrcfile
from PIL import Image
import numpy as np
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askinteger, askfloat
from tkinter import messagebox  # For warning dialog

# Function to normalize data and convert to 8-bit image
def convert_mrcs_stack_to_grid(mrc_file, grid_rows, grid_cols, scale_factor):
    # Open the .mrcs file
    with mrcfile.open(mrc_file, permissive=True) as mrc:
        data = mrc.data

    # Check the shape of the data
    print(f"Original data shape: {data.shape}")
    
    # Get the number of images in the stack (assuming the first dimension is the number of images)
    num_classes = data.shape[0]
    print(f"Number of class averages: {num_classes}")

    # Check if the grid size is sufficient
    total_cells = grid_rows * grid_cols
    if total_cells < num_classes:
        # Display a warning if some class images will be cut off
        messagebox.showwarning(
            "Grid Size Warning", 
            f"Selected grid ({grid_rows} rows and {grid_cols} columns) can only display {total_cells} images. "
            f"Some data will be cut off as there are {num_classes} class averages."
        )

    # Calculate the size of each class image and apply scaling
    class_image_height, class_image_width = data[0].shape
    scaled_height = int(class_image_height * scale_factor)
    scaled_width = int(class_image_width * scale_factor)

    # Create a new blank image to serve as the grid canvas
    grid_image_width = grid_cols * scaled_width
    grid_image_height = grid_rows * scaled_height
    grid_image = Image.new('L', (grid_image_width, grid_image_height), color=0)  # 'L' for grayscale

    # Loop through each class average, resize, and place it in the grid
    for i in range(min(num_classes, grid_rows * grid_cols)):  # Limit to the grid size
        class_image = data[i]  # Extract the i-th class average

        # Check if the image has a non-zero range, if not skip normalization
        if np.ptp(class_image) == 0:
            normalized_data = class_image.astype(np.uint8)  # No normalization needed, just convert
        else:
            # Normalize the class image
            normalized_data = (255 * (class_image - np.min(class_image)) / np.ptp(class_image)).astype(np.uint8)

        # Convert to Image object and resize it
        img = Image.fromarray(normalized_data)
        img = img.resize((scaled_width, scaled_height), Image.Resampling.LANCZOS)

        # Calculate the position in the grid
        row = i // grid_cols
        col = i % grid_cols
        position = (col * scaled_width, row * scaled_height)

        # Paste the scaled image onto the grid
        grid_image.paste(img, position)
        print(f'Class {i + 1} placed at position {position}')

    # Save the final grid image in the same directory as the input file
    output_dir = os.path.dirname(mrc_file)
    output_file = os.path.join(output_dir, f"{os.path.basename(mrc_file).replace('.mrcs', '')}_grid.png")
    grid_image.save(output_file)
    print(f'Grid image saved as {output_file}')

# Create a Tkinter root window and hide it
root = Tk()
root.withdraw()  # We don't want a full GUI, so keep the root window from appearing

# Ask the user to select an .mrc or .mrcs file
mrc_file = askopenfilename(title="Select .mrc or .mrcs file", filetypes=[("MRC files", "*.mrc *.mrcs")])

# If the user selected a file, ask for grid and scale settings
if mrc_file:
    # Ask the user to define the grid layout and scale factor
    grid_rows = askinteger("Grid Rows", "Enter the number of rows in the grid:")
    grid_cols = askinteger("Grid Columns", "Enter the number of columns in the grid:")
    scale_factor = askfloat("Scale Factor", "Enter the scaling factor for the images (e.g., 1.0 for original size):")

    # Convert and create the grid
    convert_mrcs_stack_to_grid(mrc_file, grid_rows, grid_cols, scale_factor)
else:
    print("No file selected.")
