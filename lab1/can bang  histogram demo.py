import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('rudi.jpg', 0)
img_equal_hist = cv2.equalizeHist(img)

f, axes = plt.subplots(2,2, figsize=(30,20))
axes[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0, 0].set_title('origin')
axes[0, 1].imshow(cv2.cvtColor(img_equal_hist, cv2.COLOR_BGR2RGB))
axes[0, 1].set_title('hist equal')
axes[1, 0].hist(img.flatten(), 256, [0,256])
axes[1, 1].hist(img_equal_hist.flatten(), 256, [0,256])
plt.show()
plt.close()



# import numpy as np
# import scipy.misc, math
# from scipy.misc.pilutil import Image

# img = Image.open('rudi.jpg').convert('L')

# # img is converted to an ndarray
# img1 = scipy.misc.fromimage(img)
# # 2D array is convereted to an 1D
# fl = img1.flatten()
# # histogram and the bins of the image are computed
# hist,bins = np.histogram(img1,256,[0,255])
# # cumulative distribution function is computed
# cdf = hist.cumsum()
# # places where cdf=0 is masked or ignored and
# # rest is stored in cdf_m
# cdf_m = np.ma.masked_equal(cdf,0)
# # histogram equalization is performed
# num_cdf_m = (cdf_m - cdf_m.min())*255
# den_cdf_m = (cdf_m.max()-cdf_m.min())
# cdf_m = num_cdf_m/den_cdf_m
# # the masked places in cdf_m are now 0
# cdf = np.ma.filled(cdf_m,0).astype('uint8')

# im2 = cdf[fl]

# im3 = np.reshape(im2,img1.shape)

# im4 = scipy.misc.toimage(im3)

# im4.save('hequalization_output.png')