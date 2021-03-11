# Một trong những phép biến đổi mức xám là Phép biến đổi lôgarit.
# Nó được định nghĩa là s = c * log (r + 1),
# trong đó 's' và 'r' lần lượt là giá trị pixel của đầu ra và hình ảnh đầu vào và 'c' là một hằng số.
import cv2 
import numpy as np 

img = cv2.imread('rudi.jpg')  
c = 255/(np.log(1 + np.max(img))) 
log_transformed = c * np.log(1 + img) 
  
# chỉ định dưx liêụ
log_transformed = np.array(log_transformed, dtype = np.uint8) 
  
cv2.imwrite('log_transformed.jpg', log_transformed)

cv2.imshow('log_transformed',log_transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()