# ASCII Image Converter

## Overview
This Python script converts an image into an ASCII art representation. It loads an image, resizes it while maintaining aspect ratio, converts it to grayscale, and maps pixel brightness to ASCII characters to generate the final output.

## Features
- Converts images into ASCII art.
- Resizes images while maintaining aspect ratio.
- Converts images to grayscale for better character mapping.
- Saves ASCII output to a text file.

## Prerequisites
Ensure you have Python installed along with the required dependencies:
```sh
pip install pillow numpy
```

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/ascii-image-converter.git
   ```
2. Navigate to the project directory:
   ```sh
   cd ascii-image-converter
   ```
3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Place an image file (e.g., `image.jpg`) in the project directory.
2. You can also change the path to the image by changing the path in the code.
3. Run the script:
   ```sh
   python script.py
   ```
4. The ASCII art will be saved in `image_ascii.txt`.

## Configuration
- Modify `new_width` in the script to change image resolution.
- Adjust `ascii_chars` to customize character density.

