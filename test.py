import cv2
import matplotlib.pyplot as plot
import numpy as np

foo = 34
rice_orig = cv2.imread('images/rice2.png')
rice_orig = cv2.cvtColor(rice_orig, cv2.COLOR_BGR2GRAY)
width = len(rice_orig[0])

def prout(foo: int):
    return foo + 1

# Add some blur to remove noise
rice_blur = cv2.convertScaleAbs(rice_orig, alpha=1, beta = 0)
rice_blur = cv2.GaussianBlur(rice_blur, (5,5), 5)

# Threshold the image using mean thresholding
rice_ad = cv2.adaptiveThreshold(rice_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 31, 0)

# We need to add some border around the image to segment it correctly, filled with zeroes
rice_ad = cv2.copyMakeBorder(rice_ad, top=20, bottom=20, right=20, left=20, borderType=cv2.BORDER_CONSTANT, value=[0])

# Apply some topolgy operators
kernel = np.ones((3,3), np.uint8)