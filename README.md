# Rename_images
## About
Rename_images is a Python script for renaming images based on their directory. It is designed to rename images from digital cameras or phones so that their names are more meaningful than the default name given by the camera or phone. 

** PLEASE NOTE: Rename_images is one of my first scripts written as a beginner programmer and so I apologise if the code is inelegant, unconventional or otherwise sub-optimal; it works for the intended purpose and I provide it in case it might be useful to others, but with no guarantees. **

## Requirements
Rename_images requires Python.

## Usage
Rename_images should be run in a directory containing sub-directories of images. The images may be contained in any number of levels of sub-directories.

## Example
To rename all images in sub-directories of the directory Images, the command would be:

    ./rename_images.py

## Output
Rename_images renames the image files in any sub-directories of the directory in which it is run. The images are renamed so that their name is the name of the directory in which they are immediately contained, followed by a number. The assigned numbers are based on the order in which the images are processed (usually based on the alphabetical order of their original names).
