import cv2  # import thư viện OpenCV
import numpy as np #import thư viện numpy để làm việc với dữ liệu kiểu mảng
import matplotlib.pyplot as plt # import thư viện matplotlib để vẽ ảnh

# Định nghĩa hàm lọc trung bình
def loc_trung_binh(img, mask):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            temp = img[i - 1, j - 1] * mask[0, 0] + img[i - 1, j] * mask[0, 1] + img[i - 1, j + 1] * mask[0, 2] + img[
                i, j - 1] * mask[1, 0] + img[i, j] * mask[1, 1] + img[i, j + 1] * mask[1, 2] + img[i + 1, j - 1] * mask[
                       2, 0] + img[i + 1, j] * mask[2, 1] + img[i + 1, j + 1] * mask[2, 2]
            img_new[i, j] = temp
    img_new = img_new.astype(np.uint8)
    return img_new
def run():
    # Tạo ma trận lọc trung bình 3 x 3
    mask3x3 = np.ones((3, 3), dtype="float") * (1.0 / (3 * 3))

    # Tạo ma trận lọc trung bình 11 x 11
    mask11x11 = np.ones((11, 11), dtype="float") * (1.0 / (11 * 11))

    # Tạo ma trận lọc trung bình 21 x 21
    mask21x21 = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))

    fig = plt.figure(figsize=(16, 9)) # Tạo vùng vẽ tỷ lệ 16:9
    (ax1, ax2, ax3, ax4) = fig.subplots(1, 4) # Tạo 4 vùng vẽ con

    # Đọc và hiển thị ảnh gốc
    image = cv2.imread('g2.jpg', 0)
    ax1.imshow(image, cmap='gray')
    ax1.set_title("ảnh gốc")

    # Lọc và hiển thị ảnh bằng ma trận 3 x 3
    imagenew3x3 = loc_trung_binh(image, mask3x3) #Gọi hàm lọc
    ax2.imshow(imagenew3x3, cmap='gray')
    ax2.set_title("ảnh lọc 3x3")

    # Lọc và hiển thị ảnh bằng ma trận 11 x 11
    imagenew11x11 = loc_trung_binh(image, mask11x11) #Gọi hàm lọc
    ax3.imshow(imagenew11x11, cmap='gray')
    ax3.set_title("ảnh lọc 11x11")

    # Lọc và hiển thị ảnh bằng ma trận 21 x 21
    imagenew21x21 = loc_trung_binh(image, mask21x21) #Gọi hàm lọc
    ax4.imshow(imagenew21x21, cmap='gray')
    ax4.set_title("ảnh lọc 21x21")

    # Hiển thị vùng vẽ
    plt.show()
run()