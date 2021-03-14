import cv2
# Note that the image will be read as a numpy ndarray.
anh_goc = cv2.imread('rudi.jpg')
anh_xam = cv2.cvtColor(anh_goc, cv2.COLOR_BGR2GRAY)
(threah,anh_den_trang) = cv2.threshold(anh_xam,127,255,cv2.THRESH_BINARY)

cv2.imshow("Anh Xam",anh_xam)
cv2.imwrite('rudi_xam.jpg',anh_xam)
cv2.imshow("Anh den trang", anh_den_trang)

cv2.waitKey(0)
cv2.destroyAllWindows()