import mrcfile
from PIL import Image
import numpy as np
import os  # Import os to work with file paths
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Function to normalize data and convert to 8-bit image
def convert_mrcs_stack_to_png(mrc_file):
    # Open the .mrcs file
    with mrcfile.open(mrc_file, permissive=True) as mrc:
        data = mrc.data

    # Check the shape of the data
    print(f"Original data shape: {data.shape}")
    
    # Get the number of images in the stack (assuming the third dimension is the number of images)
    num_classes = data.shape[0]
    print(f"Number of class averages: {num_classes}")

    # Get the directory where the input file is located
    output_dir = os.path.dirname(mrc_file)

    # Loop through each class average and save it as a PNG
    for i in range(num_classes):
        class_image = data[i]  # Extract the i-th class average

        # Normalize the class image
        normalized_data = (255 * (class_image - np.min(class_image)) / np.ptp(class_image)).astype(np.uint8)

        # Convert to PNG
        img = Image.fromarray(normalized_data)
        
        # Save the image as PNG with a unique name in the same directory as the input file
        output_file = os.path.join(output_dir, f"{os.path.basename(mrc_file).replace('.mrcs', '')}_class_{i + 1}.png")
        img.save(output_file)
        print(f'Class {i + 1} saved as {output_file}')

# Create a Tkinter root window and hide it
root = Tk()
root.withdraw()  # We don't want a full GUI, so keep the root window from appearing

# Ask the user to select an .mrc or .mrcs file
mrc_file = askopenfilename(title="Select .mrc or .mrcs file", filetypes=[("MRC files", "*.mrc *.mrcs")])

# If the user selected a file, proceed with conversion
if mrc_file:
    convert_mrcs_stack_to_png(mrc_file)
else:
    print("No file selected.")





