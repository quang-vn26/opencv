import numpy as np
import cv2
img = cv2.imread('rudi.jpg',0)
lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
         lst.append(np.binary_repr(img[i][j] ,width=8))

'''
# Chúng tôi có một danh sách các chuỗi trong đó mỗi chuỗi đại diện cho giá trị pixel nhị phân. 
Để trích xuất các mặt phẳng bit, 
chúng ta cần lặp qua các chuỗi và lưu trữ các ký tự tương ứng với các mặt phẳng bit vào danh sách.
# Nhân với 2 ^ (n-1) và định hình lại để tạo lại hình ảnh bit.
'''
eight_bit_img = (np.array([int(i[0]) for i in lst],dtype = np.uint8) * 128).reshape(img.shape[0],img.shape[1])
seven_bit_img = (np.array([int(i[1]) for i in lst],dtype = np.uint8) * 64).reshape(img.shape[0],img.shape[1])
six_bit_img = (np.array([int(i[2]) for i in lst],dtype = np.uint8) * 32).reshape(img.shape[0],img.shape[1])
five_bit_img = (np.array([int(i[3]) for i in lst],dtype = np.uint8) * 16).reshape(img.shape[0],img.shape[1])
four_bit_img = (np.array([int(i[4]) for i in lst],dtype = np.uint8) * 8).reshape(img.shape[0],img.shape[1])
three_bit_img = (np.array([int(i[5]) for i in lst],dtype = np.uint8) * 4).reshape(img.shape[0],img.shape[1])
two_bit_img = (np.array([int(i[6]) for i in lst],dtype = np.uint8) * 2).reshape(img.shape[0],img.shape[1])
one_bit_img = (np.array([int(i[7]) for i in lst],dtype = np.uint8) * 1).reshape(img.shape[0],img.shape[1])

#Concatenate những hình ảnh này để dễ hiển thị bằng cv2.hconcat ()
finalr = cv2.hconcat([eight_bit_img,seven_bit_img,six_bit_img,five_bit_img])
finalv =cv2.hconcat([four_bit_img,three_bit_img,two_bit_img,one_bit_img])

# Nối theo chiều dọc
final = cv2.vconcat([finalr,finalv])

cv2.imshow('a',final)

# Kết hợp các mặt phẳng 4 bit
new_img = eight_bit_img+seven_bit_img+six_bit_img+five_bit_img

cv2.imshow('a2',new_img)
cv2.waitKey(0)

# cv2.waitKey(0) 