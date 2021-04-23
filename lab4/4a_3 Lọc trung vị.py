import cv2  # import thư viện OpenCV
import numpy as np #import thư viện numpy để làm việc với dữ liệu kiểu mảng
import matplotlib.pyplot as plt # import thư viện matplotlib để vẽ ảnh


# Định nghĩa hàm lọc trung vị
def loc_trung_vi(img):
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
          
            temp = sorted(temp) 
            img_new[i, j]= temp[4] 
    img_new = img_new.astype(np.uint8)
    return img_new


# Đọc và hiển thị ảnh gốc
image = cv2.imread('g2.jpg', 0)
# Lọc trung vị 3 x 3 và hiển thị ảnh
imagenew = loc_trung_vi(image) #Gọi hàm lọc

f, axes = plt.subplots(2,2, figsize=(30,20))
axes[0, 0].imshow(image, cmap='gray')
axes[0, 0].set_title('Gốc')
axes[0, 1].imshow(imagenew, cmap='gray')
axes[0, 1].set_title('Lọc Trung Vị')
axes[1, 0].hist(image.flatten(), 256, [0,256])
axes[1, 1].hist(imagenew.flatten(), 256, [0,256])
plt.show()
plt.close()

