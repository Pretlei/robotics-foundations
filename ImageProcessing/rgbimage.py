import cv2
import matplotlib.pyplot as plt

#load image as BGR
img_bgr = cv2.imread("C:/Users/Presl/Projects/1A_Robotics/ImageProcessing/sealion.jpg") 

if img_bgr is None: # check if image loaded
    print("could not load image!")
else:
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB) # make image rgb for display

plt.imshow(img_rgb)
plt.axis("off")
plt.title("Sealion")
plt.show()
