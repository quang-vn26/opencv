#python 3.7.4,opencv4.1
#  https://blog.csdn.net/caimouse/article/details/51749579
#
import cv2
import numpy as np
from scipy import signal
 
 #Path of the picture
imgname ='../data/g2.jpg'
 
 #Read the picture
image = cv2.imread(imgname, cv2.IMREAD_GRAYSCALE)
 
 #Image height and width
h,w = image.shape[:2]
print('imagesize={}-{}'.format(w,h))
 
 #Show original image
cv2.imshow("Image",image)
 
 #operator
sigma=2
K = 1.1
g1 = cv2.GaussianBlur(image, (23,23), sigmaX=sigma,sigmaY=sigma)
g2 = cv2.GaussianBlur(image, (23,23), sigmaX=sigma*K,sigmaY=sigma*K)
 
DOG = g2 - g1
DOG[DOG>0]=255
DOG[DOG<=0]=0
DOG = DOG.astype(np.uint8)
cv2.imshow("DOG",DOG)
 
cv2.waitKey(0)
cv2.destroyAllWindows()