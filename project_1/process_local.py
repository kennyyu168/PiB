"""
ECE196 Face Recognition Project
Author: Will Chen

Prerequisite: You need to install OpenCV before running this code
The code here is an example of what you can write to print out 'Hello World!'
Now modify this code to process a local image and do the following:
1. Read geisel.jpg
2. Convert color to gray scale
3. Resize to half of its original dimensions
4. Draw a box at the center the image with size 100x100
5. Save image with the name, "geisel-bw-rectangle.jpg" to the local directory
All the above steps should be in one function called process_image()
"""

# Import OpenCV
import cv2

# Edit this function
def process_image():

    # Reads in the image 
    image_read = cv2.imread("geisel.jpg")

    # Converts the image to greyscale
    grey = cv2.cvtColor(image_read, cv2.COLOR_RGB2GRAY)
    
    # Resizes the image to half it's dimensions
    width = int(grey.shape[1] * 0.5)
    height = int(grey.shape[0] * 0.5)
    dim = (width, height)
    resized = cv2.resize(grey, dim, interpolation = cv2.INTER_AREA)

    # Draws a box at the center of the image 
    top_corner_x = ( width / 2 ) - 50
    top_corner_y = ( height / 2 ) - 50
    bottom_corner_x = ( width / 2 ) + 50
    bottom_corner_y = ( height / 2 ) + 50
    boxed = cv2.rectangle( resized, (top_corner_x, top_corner_y), (bottom_corner_x, bottom_corner_y), (255, 255, 255), 3) 

    # Save image 
    cv2.imwrite( "geisel-bw-rectangle.jpg", boxed )


# Call process_image function.
def main():
    process_image()


if(__name__ == '__main__'):
    main()
