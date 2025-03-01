# Bayer Filter and Demosaicing in Python

## Overview
This project implements a Bayer filter simulation, applies demosaicing (color interpolation), and converts the result to the HSV color space. It visualizes all intermediate steps to understand the image processing pipeline.

## Features
- Generates a **random grayscale image** (0-255 intensity values).
- Creates a **Bayer filter pattern** (RGGB arrangement).
- **Maps** the correct color values and interpolates missing ones.
- Applies **demosaicing** using interpolation techniques.
- Converts the final image to **HSV color space**.
- Displays all inputs and outputs for visualization.

## Installation
Ensure you have Python 3.x installed and install required dependencies using:

```sh
pip install numpy matplotlib opencv-python
```

If OpenCV fails to install, try:

```sh
pip install opencv-python-headless
```

## Usage
Run the Jupyter Notebook to execute all steps.


## Explanation
### What is a Bayer Filter?
A **Bayer filter** is a color filter array used in digital cameras to capture RGB values. It follows an RGGB (Red-Green-Green-Blue) pattern where each pixel records only **one color**.

### How is Demosaicing Performed?
Demosaicing uses **linear interpolation** (or other advanced methods) to estimate missing color values based on neighboring pixels.

## Alternative Interpolation Methods
- **Bilinear (Fast, used by OpenCV by default)**
- **Bicubic (Smoother results, slightly slower)**
- **Lanczos (Sharper images, best for high-res images)**
- **Edge-Aware Interpolation (Best for natural images)**

## Conclusion
This project demonstrates **Bayer filtering, demosaicing, and color space conversion** in Python using OpenCV and NumPy. You can modify the interpolation method to test different results!

## License
This project is open-source under the MIT License.