import scipy as sp
import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('../data/g2.jpg',0)
LoG = nd.gaussian_laplace(img, 2)
thres = np.absolute(LoG).mean() * 0.75
output = sp.zeros(LoG.shape)
w = output.shape[1]
h = output.shape[0]

for y in range(1, h - 1):
    for x in range(1, w - 1):
        patch = LoG[y-1:y+2, x-1:x+2]
        p = LoG[y, x]
        maxP = patch.max()
        minP = patch.min()
        if (p > 0):
            zeroCross = True if minP < 0 else False
        else:
            zeroCross = True if maxP > 0 else False
        if ((maxP - minP) > thres) and zeroCross:
            output[y, x] = 1
#chuyen ve mau xam
# img=rgb2gray(img);
#hien thi histogram
# imhist(img);
# hist = cv2.calcHist([img],[0],None,[256],[0,256])

plt.subplot(131),plt.imshow(img,cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(output,cmap='gray'),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
# plt.subplot(133),plt.hist(img),plt.title('histogram 1')
# plt.xticks([]), plt.yticks([])
plt.show()
# cv2.show() 