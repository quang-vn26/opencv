import cv2 
import numpy as np 
# https://www.geeksforgeeks.org/point-processing-in-image-processing-using-python-opencv/
img = cv2.imread('food.png',0) 

# Để xác định tổng số
# hàng và cột của hình ảnh,
# kích thước của hình ảnh
m,n = img.shape 

# Để tìm mức xám tối đa
# giá trị trong hình ảnh 
L = img.max() 

# Giá trị mức xám tối đa trừ
# hình ảnh ban đầu cung cấp cho
# hình ảnh âm bản
img_neg = L-img 

# giá trị ngưỡng thấp hơn
T1 = 100

# giá trị ngưỡng trên
T2 = 180

# tạo một mảng các số không
img_thresh_back = np.zeros((m,n), dtype = int) 

for i in range(m): 
	
	for j in range(n): 
		
		if T1 < img[i,j] < T2: 
			img_thresh_back[i,j]= 255
		else: 
			img_thresh_back[i,j] = img[i,j] 

# Chuyển mảng sang hình ảnh png
cv2.imwrite('Cameraman_Thresh_Back.png', img_thresh_back) 
cv2.imshow('Hi', img_thresh_back)
cv2.waitKey(0)
cv2.destroyAllWindows()
