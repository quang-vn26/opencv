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
   cv2.imwrite("s_noise_image.png",noise_image) #imwrite(name,file)
   return noise_image


def gaussian_noise(img):
	noise_img = random_noise(img, mode='gaussian')
	noise_image=noise_img*255
	
	return noise_image

def max_filter(image):
    kSize = 3
    bSize = kSize // 2 
    image = cv2.copyMakeBorder(image, bSize, bSize, bSize, bSize, cv2.BORDER_CONSTANT, 0)
    imageO = np.zeros(image.shape, dtype=np.uint8)
    for x in range(image.shape[0] - kSize + 1):
	    for y in range(image.shape[1] - kSize + 1):
	        imageO[x, y] = np.amax(image[x:x+kSize, y:y+kSize])
    return imageO        
def min_filter(image):
	kSize = 3
	bSize = kSize // 2 
	image = cv2.copyMakeBorder(image, bSize, bSize, bSize, bSize, cv2.BORDER_CONSTANT, 0)
	imageO = np.zeros(image.shape, dtype=np.uint8)
	for x in range(image.shape[0] - kSize + 1):
		for y in range(image.shape[1] - kSize + 1):
			imageO[x, y] = np.amax(image[x:x+kSize, y:y+kSize])
	return imageO        
def mid_point(image):
	kSize = 3
	bSize = kSize // 2 
	image = cv2.copyMakeBorder(image, bSize, bSize, bSize, bSize, cv2.BORDER_CONSTANT, 0)
	imageO = np.zeros(image.shape, dtype=np.uint8)
	for x in range(image.shape[0] - kSize + 1):
		for y in range(image.shape[1] - kSize + 1):
			imageO[x, y] = (np.amax(image[x:x+kSize, y:y+kSize])+np.amax(image[x:x+kSize, y:y+kSize]))/2
	return imageO

img = cv2.imread("g2.jpg",0)
print(img)
#print(img)
# GuassNoiseImg = gaussian_noise(img)
GuassNoiseImg = gaussian_noise(img)
cv2.imwrite("guass_noise_image.png",GuassNoiseImg) #imwrite(name,file)

ppImg = pepper_noise(img)
cv2.imwrite("pepper_noise_image.png",ppImg)

saltImg = salt_noise(img)
cv2.imwrite("salt_noise_image.png",saltImg) #imwrite(name,file)

maxImg = max_filter(ppImg)
minImg = min_filter(saltImg)
mid_pointImg = mid_point(GuassNoiseImg)


f, axes = plt.subplots(2,4, figsize=(30,20))
axes[0, 0].imshow(maxImg, cmap='gray')
# axes[0, 0].set_title('Loc Max')
# axes[0, 0].set_title('Loc Min')
axes[0, 0].set_title('Loc Midpoit')


axes[0, 1].imshow(GuassNoiseImg, cmap='gray')
axes[0, 1].set_title('Nhieu Gauss')

axes[0, 2].imshow(ppImg, cmap='gray')
axes[0, 2].set_title('Nhieu Tieu')

axes[0, 3].imshow(saltImg, cmap='gray')
axes[0, 3].set_title('Nhieu Muoi')

# axes[0, 4].imshow(maxImg, cmap='gray')
# axes[0, 4].set_title('Loc Max')

# axes[1, 0].hist(maxImg.flatten(), 256, [0,256])
# axes[1, 0].hist(minImg.flatten(), 256, [0,256])
axes[1, 0].hist(mid_pointImg.flatten(), 256, [0,256])


axes[1, 1].hist(GuassNoiseImg.flatten(), 256, [0,256])

axes[1, 2].hist(ppImg.flatten(), 256, [0,256])

axes[1, 3].hist(saltImg.flatten(), 256, [0,256])

# axes[1, 4].hist(maxImg.flatten(), 256, [0,256])

plt.show()
plt.close()

