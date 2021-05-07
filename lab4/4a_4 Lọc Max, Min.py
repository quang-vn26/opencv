import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import random
from skimage.util import random_noise

def pepper_noise(img):
	noise_img = random_noise(img, mode='pepper')
	noise_image=noise_img*255
   # print(noise_image[0])
	return noise_image

def salt_noise(img):
   noise_img = random_noise(img, mode='salt') #s&p
   noise_image=noise_img*255
   return noise_image


def gaussian_noise(img):
	noise_img = random_noise(img, mode='gaussian')
	noise_image=noise_img*255
	return noise_image
def max_filter(img,a):
   return cv2.max(img,a)
def min_filter(img,a):
   return cv2.min(img,a)   

img = cv2.imread("g2.jpg",0)
print(img)
#print(img)
# GuassNoiseImg = gaussian_noise(img)
GuassNoiseImg = gaussian_noise(img)
ppImg = pepper_noise(img)
saltImg = salt_noise(img)
maxImg = max_filter(ppImg,100)
minImg = min_filter(saltImg,100)



f, axes = plt.subplots(2,4, figsize=(30,20))
axes[0, 0].imshow(maxImg, cmap='gray')
axes[0, 0].set_title('Loc Max')

axes[0, 1].imshow(GuassNoiseImg, cmap='gray')
axes[0, 1].set_title('Nhieu Gauss')

axes[0, 2].imshow(ppImg, cmap='gray')
axes[0, 2].set_title('Nhieu Tieu')

axes[0, 3].imshow(saltImg, cmap='gray')
axes[0, 3].set_title('Nhieu Muoi')

# axes[0, 4].imshow(maxImg, cmap='gray')
# axes[0, 4].set_title('Loc Max')

axes[1, 0].hist(maxImg.flatten(), 256, [0,256])

axes[1, 1].hist(GuassNoiseImg.flatten(), 256, [0,256])

axes[1, 2].hist(ppImg.flatten(), 256, [0,256])

axes[1, 3].hist(saltImg.flatten(), 256, [0,256])

# axes[1, 4].hist(maxImg.flatten(), 256, [0,256])

plt.show()
plt.close()

