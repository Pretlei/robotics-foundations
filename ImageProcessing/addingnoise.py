import matplotlib.pyplot as plt
import numpy as np
import cv2
from rgbimage import img_rgb

# for real hardware practice

# Gaussian Noise, more realistic for robotics

# mean=0 means the brightness level of the image will be the same
# if one pixel's brightness goes up, another's will go down
# higher the std value, more noisier the image
def add_gaussian_noise(image, mean=0, std=20): 
    noise = np.random.normal(mean, std, image.shape) # adds noise to each pixel each channel (R, G, B)
    noisy = image + noise # makes new image with noise
    return np.clip(noisy, 0, 255).astype(np.uint8) # caps noise between 0 to 250 incase it goes over
    # converts image to uint8 type for numpy

noisy_img = add_gaussian_noise(img_rgb)

plt.imshow(noisy_img)
plt.title("Noisy Sealion")
plt.axis("off")
plt.show()

# Salt and Pepper Noise, set pixels to black and white (transmission error)

def add_salt_pepper(image, prob=0.01): #probability that a pixel is corrupted is 1% here
    noisy = image.copy()
    # generates random values between 0 and 1 for each pixel (channels don't matter)
    mask = np.random.rand(*image.shape[:2])

    noisy[mask < prob] = 0        # pepper
    noisy[mask > 1 - prob] = 255  # salt
    return noisy

sp_img = add_salt_pepper(img_rgb)

plt.imshow(sp_img)
plt.title("Sprinkled Sealion")
plt.axis("off")
plt.show()