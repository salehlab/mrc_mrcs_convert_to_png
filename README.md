# mrcs_to_png_tools
Easily convert .mrcs files to PNG images, either saving all classes as separate images or arranging them in a grid format.


This repository contains two Python scripts to help you convert class averages from .mrcs files into PNG format:

- **mrcs_to_png_selectfile_savesallclassesgrid.py**:

  Converts class averages in .mrcs files into a single grid image where the user can specify the number of rows and columns for the grid layout, as well as the scale factor for resizing the images.
- **mrcs_to_png_selectfile_saveseperateclasses.py**:

  Converts class averages in .mrcs files into separate PNG images, one per class average.

## Prerequisites

Make sure you have the following installed in your Python environment before running the script::

  - mrcfile: For reading .mrcs files.
  - Pillow (PIL): For creating and manipulating images.
  - numpy: For handling numerical data from the .mrcs files.

   ```bash
pip install mrcfile Pillow numpy
  ```

## Installation

Clone this repository to your local machine:

  ```bash
git clone https://github.com/salehlab/mrcs_to_png_tools.git
  ```

### Ensure the Script is in your PATH

To run the script from anywhere, add the script directory to your PATH environment variable:

  ```bash
chmod +x mrcs_to_png_selectfile_savesallclassesgrid.py
chmod +x mrcs_to_png_selectfile_saveseperateclasses.py
  ```

If the script is not already executable, you can make it executable by running:

  ```bash
chmod +x mrcs_to_png_selectfile_savesallclassesgrid.py
chmod +x mrcs_to_png_selectfile_saveseperateclasses.py
  ```

## Usage

**1. mrcs_to_png_selectfile_savesallclassesgrid.py**

This script converts the .mrcs file into a single PNG grid image, where all class averages are arranged in a grid of user-specified rows and columns.

To run the script:

  ```bash
python mrcs_to_png_selectfile_savesallclassesgrid.py
  ```

You will be prompted for:
  - Selecting the .mrcs file.
  - Entering the number of rows and columns for the grid.
  - Entering a scaling factor for resizing the images.

**2. mrcs_to_png_selectfile_saveseperateclasses.py**

This script converts each class average in the .mrcs file into a separate PNG file and saves them in the same directory as the input file.

To run the script:

  ```bash
python mrcs_to_png_selectfile_saveseperateclasses.py
  ```

You will be prompted for:
  - Selecting the .mrcs file.
  - Each class average will be saved as a separate PNG file.

## Contributing
We welcome contributions! Feel free to submit pull requests or open an issue if you find bugs or have suggestions.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
