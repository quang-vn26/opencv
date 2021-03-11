import cv2 
import numpy as np 
# s=c*r^y opencv
img = cv2.imread('rudi.jpg')  
c = 255/(np.log(1 + np.max(img)))
r = 2
y = 1
so_mu = c * np.log(1 + img) 
  
# chỉ định dưx liêụ
so_mu = np.array(so_mu, dtype = np.uint8) 
  
cv2.imwrite('bien_doi_ham_mu.jpg', so_mu)

cv2.imshow('rudi',so_mu)

cv2.waitKey(0)
cv2.destroyAllWindows()