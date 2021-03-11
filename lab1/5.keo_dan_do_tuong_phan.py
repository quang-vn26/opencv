# Kéo giãn độ tương phản là một kỹ thuật nâng cao hình ảnh đơn giản cố gắng cải thiện độ tương phản trong hình ảnh bằng cách kéo dài phạm vi giá trị cường độ mà nó chứa để mở rộng phạm vi giá trị mong muốn.
import cv2 
import numpy as np 
  
# Function to map each intensity level to output intensity level. 
# Chức năng ánh xạ từng mức cường độ thành mức cường độ đầu ra.
def pixelVal(pix, r1, s1, r2, s2): 
    if (0 <= pix and pix <= r1): 
        return (s1 / r1)*pix 
    elif (r1 < pix and pix <= r2): 
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1 
    else: 
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2 
  

img = cv2.imread('rudi.jpg') 
r1 = 70
s1 = 0
r2 = 140
s2 = 255
  
# Vectorize the function to apply it to each value in the Numpy array. 
# Vectorize hàm để áp dụng nó cho từng giá trị trong mảng Numpy.
pixelVal_vec = np.vectorize(pixelVal) 
   
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2) 
 
cv2.imwrite('contrast_stretch.jpg', contrast_stretched) 

cv2.imshow('contrast_stretch',contrast_stretched)

cv2.waitKey(0)
cv2.destroyAllWindows()