# https://en.wikipedia.org/wiki/Contraharmonic_mean
# https://stackabuse.com/introduction-to-image-processing-in-python-with-opencv/
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
	return noise_image
def gaussian_noise(img):
	noise_img = random_noise(img, mode='gaussian')
	noise_image=noise_img*255
	return noise_image

def noisy(noise_typ,image):
   if noise_typ == "gauss":
      row,col,ch= image.shape
      mean = 0
      var = 0.1
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      return noisy
   elif noise_typ == "s&p":
      row,col,ch = image.shape
      s_vs_p = 0.5
      amount = 0.004
      out = np.copy(image)
      # Salt mode
      num_salt = np.ceil(amount * image.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
      out[coords] = 1

      # Pepper mode
      num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
      out[coords] = 0
      return out

# ----- Viet ham loc
def harmonicMean(img):
   # n=len(arr)
   # sm = 0
   # for i in range(0,n):
   #    sm=sm+(1)/arr[i]
   # return n/sm   

   m, n = img.shape
   img_new = np.zeros([m, n])
   for i in range(1, m-1): 
       for j in range(1, n-1): 
         temp = [img[i-1, j-1], 
                  img[i-1, j], 
                  img[i-1, j + 1], 
                  img[i, j-1], 
                  img[i, j], 
                  img[i, j + 1], 
                  img[i + 1, j-1], 
                  img[i + 1, j], 
                  img[i + 1, j + 1]] 
         # Bo loc 3.3
         t = 0
         n=9
         for q in temp:
           t=t+(1)/q
         tmp = n/t   
         img_new[i, j]= tmp
         # print(tmp)
   img_new = img_new.astype(np.uint8)
   print(img_new)
   return img_new



img = cv2.imread("g2.jpg",0)
# GuassNoiseImg = gaussian_noise(img)
GuassNoiseImg = gaussian_noise(img)
ppImg = pepper_noise(img)
harmonicMeanImg = harmonicMean(img)

f, axes = plt.subplots(2,4, figsize=(30,20))
axes[0, 0].imshow(img, cmap='gray')
axes[0, 0].set_title('Goc')

axes[0, 1].imshow(GuassNoiseImg, cmap='gray')
axes[0, 1].set_title('Nhieu Gauss')

axes[0, 2].imshow(ppImg, cmap='gray')
axes[0, 2].set_title('Nhieu Muoi')

axes[0, 3].imshow(harmonicMeanImg, cmap='gray')
axes[0, 3].set_title('Loc trung binh contraharmonic')


axes[1, 0].hist(img.flatten(), 256, [0,256])

axes[1, 1].hist(GuassNoiseImg.flatten(), 256, [0,256])

axes[1, 2].hist(ppImg.flatten(), 256, [0,256])
axes[1, 3].hist(harmonicMeanImg.flatten(), 256, [0,256])

plt.show()
plt.close()

