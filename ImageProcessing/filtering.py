import numpy as np
import matplotlib.pyplot as plt
import cv2
from addingnoise import noisy_img, sp_img, img_rgb

# Gaussian Blur (gaussian noise reduction)
#for edge detection, feature extraction

#the larger the (y, y) the heavier the blur. 5px*5px is the window through which the image is inspected
#larger the y, heavier the blur
#higher the sigmaX, the more priority the border pixels start to get compared to the centre pixel
blurred = cv2.GaussianBlur(noisy_img, (5, 5), sigmaX=1.0)

plt.imshow(blurred)
plt.title("Gaussian scolded Sealion")
plt.axis("off")
plt.show()

# median filter (for salt and pepper noise)
# for cleaning depth images
# 5 is the window size, picks the median hex in the 5x5 and applies to all pixels in the window
median = cv2.medianBlur(sp_img, 3)

plt.imshow(median)
plt.title("Washed Sealion")
plt.axis("off")
plt.show()

# edge-preserving filter (bilateral)
# d is diameter of window
# sigmaColor = the difference between the centre pixel's and the neighbouring pixel's colour for the pixel to be
# considered an edge
# sigmaSpace = how far away a pixel can be to influence the centre pixel, within the diameter
bilateral = cv2.bilateralFilter(img_rgb, d=9, sigmaColor=75, sigmaSpace=75)

plt.imshow(bilateral)
plt.title("Bilateral Sealion")
plt.axis("off")
plt.show()

