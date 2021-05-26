import cv2
from scipy.ndimage import imread
import matplotlib.pyplot as plt
import numpy as np
from skimage.util import random_noise
from skimage.filters import rank

img=imread("g2.jpg",False,'L')
img=img.astype(np.uint8)
img_2=img.copy()
rows,cols=img.shape[:2]
plt.title("Original Image")
plt.imshow(img,plt.cm.gray)
plt.show()