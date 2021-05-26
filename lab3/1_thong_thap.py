import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt,exp

def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def idealFilterLP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    # print(base)
    rows, cols = imgShape[:2]
    # print("rows, cols ")
    print(rows,cols)
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            if distance((y,x),center) < D0:
                base[y,x] = 1
    return base

def butterworthLP(D0,imgShape,n):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = 1/(1+(distance((y,x),center)/D0)**(2*n))
    return base

def gaussianLP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)
    for x in range(cols):
        for y in range(rows):
            base[y,x] = exp(((-distance((y,x),center)**2)/(2*(D0**2))))
    return base

img = cv2.imread("g2.jpg", 0)
original = np.fft.fft2(img) #Fast
center = np.fft.fftshift(original)

plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)

LowPassCenter = center * idealFilterLP(50,img.shape)
LowPass = np.fft.ifftshift(LowPassCenter) #dich chuyen thanh phan 0 ddeens trung tam mang
inverse_LowPass = np.fft.ifft2(LowPass)
plt.subplot(241), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Ideal Low Pass")

LowPassCenter = center * butterworthLP(50,img.shape,10)
LowPass = np.fft.ifftshift(LowPassCenter)
inverse_LowPass = np.fft.ifft2(LowPass)
plt.subplot(242), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Butterworth Low Pass (n=10)")

LowPassCenter = center * gaussianLP(50,img.shape)
LowPass = np.fft.ifftshift(LowPassCenter)
inverse_LowPass = np.fft.ifft2(LowPass)
plt.subplot(243), plt.imshow(np.abs(inverse_LowPass), "gray"), plt.title("Gaussian Low Pass")

plt.subplot(244), plt.imshow(img, "gray"), plt.title("Origin")

plt.figure(figsize=(6.4*5, 4.8*5), constrained_layout=False)
LowPass = idealFilterLP(50,img.shape)
plt.subplot(231), plt.imshow(LowPass, "gray"), plt.title("Ideal Low Pass Filter")

LowPass = butterworthLP(50,img.shape,20)
plt.subplot(232), plt.imshow(LowPass, "gray"), plt.title("Butterworth Low Pass Filter (n=20)")

LowPass = butterworthLP(50,img.shape,3)
plt.subplot(233), plt.imshow(LowPass, "gray"), plt.title("Butterworth Low Pass Filter (n=3)")

plt.show()    