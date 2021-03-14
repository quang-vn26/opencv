import cv2 
import numpy as np 

img = cv2.imread('food.png',0) 
m,n = img.shape 
L = img.max() 
img_neg = L-img 
T1 = 100
T2 = 180
img_thresh_back = np.zeros((m,n), dtype = int) 

for i in range(m): 
	
	for j in range(n): 
		
		if T1 < img[i,j] < T2: 
			img_thresh_back[i,j]= 255
		else: 
			img_thresh_back[i,j] = img[i,j] 

cv2.imwrite('Cameraman_Thresh_Back.png', img_thresh_back) 
# cv2.imshow('Hi', img_thresh_back)
img2 = cv2.imread('Cameraman_Thresh_Back.png')
cv2.imshow('Anh Goc',img)
cv2.imshow('Cat lat muc xam',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
