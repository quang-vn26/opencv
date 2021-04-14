from tkinter.filedialog import askopenfilename, asksaveasfile
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, CheckButtons, Slider

sourceImg =''
img = ''
resultImg = ''
firstAction = False
continuousEdit = False
currentFunc = 0
kernel_size = 3
sigma = 1
def open_File():
    filename = askopenfilename(title="Select file", filetypes=(("TIF files", "*.tif"), ("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")))
    img = cv.imread(filename, 0)
    return img

def save_File(img):
    filename = asksaveasfile(mode='w', defaultextension=".png")

    if filename is None:
        return
    print(filename)
    cv.imwrite(filename.name, img)

def inverse(img):
    return 255-img

def logarit_transform(img, c):
    return float(c) * cv.log(1.0 + img)

def gamma_correction(img, gamma, c):
    return float(c) * pow(img, float(gamma))

def thresholding(img, thres):
    return img > thres

fig = plt.figure(figsize=(16, 9))
fig.canvas.manager.set_window_title('Image Processing')
plt.subplots_adjust(bottom=0.25)
class Index:
    def browse_img(self, event):
        global sourceImg
        global img
        global firstAction
        global currentFunc
        currentFunc = 0
        hideSliders()
        firstAction = False
        sourceImg = open_File()
        img = sourceImg
        ax1 = plt.subplot(1, 2, 1)
        ax1.imshow(sourceImg, cmap='gray')
        ax1.set_title("Source image")
        plt.draw()

    def save_img(self, event):
        global currentFunc
        currentFunc = 0
        hideSliders()
        save_File(resultImg)
        plt.draw()

    def inverse_img(self, event):
        global resultImg
        global firstAction
        global currentFunc
        currentFunc = 0
        hideSliders()
        if continuousEdit:
            img = resultImg
        else:
            img = sourceImg
        if firstAction is True:
            plt.cla()
        else:
            firstAction = True
        resultImg = inverse(img)
        ax2 = plt.subplot(1, 2, 2)
        ax2.imshow(resultImg, cmap='gray')
        ax2.set_title("Result image")
        plt.draw()

    def histogram(self, event):
        global resultImg
        global firstAction
        global currentFunc
        currentFunc = 0
        hideSliders()
        if continuousEdit:
            img = resultImg
        else:
            img = sourceImg
        if firstAction is True:
            plt.cla()
        else:
            firstAction = True

        resultImg = cv.equalizeHist(img)
        ax2 = plt.subplot(1, 2, 2)
        ax2.imshow(resultImg, cmap='gray')
        ax2.set_title("Result image")
        plt.draw()

    def logarit(self, event):
        global currentFunc
        hideSliders()
        if continuousEdit:
            img = resultImg
        else:
            img = sourceImg
        ax_sliderC.set_visible(True)
        currentFunc = 1

    def gamma(self, event):
        global currentFunc
        hideSliders()
        if continuousEdit:
            img = resultImg
        else:
            img = sourceImg
        ax_sliderGamma.set_visible(True)
        currentFunc = 2

    def thres(self, event):
        global currentFunc
        hideSliders()
        if continuousEdit:
            img = resultImg
        else:
            img = sourceImg
        ax_sliderThres.set_visible(True)
        currentFunc = 3

    def blur(self, event):
        global currentFunc
        hideSliders()
        if continuousEdit:
            img = resultImg
        else:
            img = sourceImg
        ax_sliderKernel.set_visible(True)
        ax_sliderSigma.set_visible(True)
        currentFunc = 4

callback = Index()

def hideSliders():
    ax_sliderC.set_visible(False)
    ax_sliderGamma.set_visible(False)
    ax_sliderThres.set_visible(False)
    ax_sliderKernel.set_visible(False)
    ax_sliderSigma.set_visible(False)

ax_top_btn1 = plt.axes([0.02, 0.92, 0.06, 0.04])
btn_browse_img = Button(ax_top_btn1, 'Browse')
btn_browse_img.on_clicked(callback.browse_img)

ax_top_btn2 = plt.axes([0.1, 0.92, 0.06, 0.04])
btn_save_img = Button(ax_top_btn2, 'Save')
btn_save_img.on_clicked(callback.save_img)

ax_checkbutton = plt.axes([0.02, 0, 0.12, 0.05])
label = ["Continuous editing"]
check_button = CheckButtons(ax_checkbutton, labels=label, actives=[0])

def checkboxChange(event):
    global continuousEdit
    continuousEdit = not continuousEdit
    print(continuousEdit)

check_button.on_clicked(checkboxChange)

ax_bot_btn1 = plt.axes([0.02, 0.05, 0.08, 0.04])
btn_inverse = Button(ax_bot_btn1, "Inverse")
btn_inverse.on_clicked(callback.inverse_img)

ax_bot_btn2 = plt.axes([0.11, 0.05, 0.1, 0.04])
btn_hist = Button(ax_bot_btn2, "Histogram equalize")
btn_hist.on_clicked(callback.histogram)

ax_bot_btn3 = plt.axes([0.22, 0.05, 0.08, 0.04])
btn_logarit = Button(ax_bot_btn3, "Logarithmic")
btn_logarit.on_clicked(callback.logarit)

ax_bot_btn4 = plt.axes([0.31, 0.05, 0.08, 0.04])
btn_gamma = Button(ax_bot_btn4, "Gamma")
btn_gamma.on_clicked(callback.gamma)

ax_bot_btn5 = plt.axes([0.40, 0.05, 0.08, 0.04])
btn_thresholding = Button(ax_bot_btn5, "Thresholding")
btn_thresholding.on_clicked(callback.thres)

ax_bot_btn6 = plt.axes([0.49, 0.05, 0.08, 0.04])
btn_blur = Button(ax_bot_btn6, "Gaussian blur")
btn_blur.on_clicked(callback.blur)

ax_sliderC = plt.axes([0.02, 0.1, 0.45, 0.04])
c_slider = Slider(ax=ax_sliderC, label='C', valmin=0.1, valmax=5.0, valinit=1, valstep=0.1, orientation="horizontal")
ax_sliderC.set_visible(False)

ax_sliderGamma = plt.axes([0.05, 0.1, 0.45, 0.04])
gamma_slider = Slider(ax=ax_sliderGamma, label='Gamma', valmin=0.1, valmax=25.0, valinit=1, valstep=0.1, orientation="horizontal")
ax_sliderGamma.set_visible(False)

ax_sliderThres = plt.axes([0.05, 0.1, 0.5, 0.04])
thres_slider = Slider(ax=ax_sliderThres, label='Thres', valmin=0, valmax=500, valinit=100, valfmt='%d', orientation="horizontal")
ax_sliderThres.set_visible(False)

ax_sliderKernel = plt.axes([0.06, 0.1, 0.4, 0.04])
kernel_slider = Slider(ax=ax_sliderKernel, label='Kernel size', valmin=1, valmax=25, valinit=3, valfmt='%d', valstep=2, orientation="horizontal")
ax_sliderKernel.set_visible(False)

ax_sliderSigma = plt.axes([0.55, 0.1, 0.4, 0.04])
sigma_slider = Slider(ax=ax_sliderSigma, label='Sigma', valmin=0.1, valmax=5, valinit=1, valfmt='%d', valstep=0.1, orientation="horizontal")
ax_sliderSigma.set_visible(False)

def updateC(val):
    global resultImg
    global firstAction
    global currentFunc
    global img
    if firstAction is True:
        plt.cla()
        # print("cleaned")
    else:
        firstAction = True
    if currentFunc == 1:
        resultImg = logarit_transform(img, val)
        ax2 = plt.subplot(1, 2, 2)
        ax2.imshow(resultImg, cmap='gray')
        ax2.set_title("Result image")
        plt.draw()
c_slider.on_changed(updateC)

def updateGamma(val):
    global resultImg
    global firstAction
    global currentFunc
    global img
    if firstAction is True:
        plt.cla()
        # print("cleaned")
    else:
        firstAction = True
    if currentFunc == 2:
        resultImg = gamma_correction(img, val, 1)
        ax2 = plt.subplot(1, 2, 2)
        ax2.imshow(resultImg, cmap='gray')
        ax2.set_title("Result image")
        plt.draw()
gamma_slider.on_changed(updateGamma)

def updateThres(val):
    global resultImg
    global firstAction
    global currentFunc
    global img
    if firstAction is True:
        plt.cla()
        # print("cleaned")
    else:
        firstAction = True
    if currentFunc == 3:
        resultImg = thresholding(img, val)
        ax2 = plt.subplot(1, 2, 2)
        ax2.imshow(resultImg, cmap='gray')
        ax2.set_title("Result image")
        plt.draw()
thres_slider.on_changed(updateThres)

def updateKernel(val):
    global resultImg
    global firstAction
    global currentFunc
    global img
    global sigma
    global kernel_size
    if firstAction is True:
        plt.cla()
    else:
        firstAction = True
    if currentFunc == 4:
        kernel_size = int(val)
        resultImg = cv.GaussianBlur(img, ksize=(kernel_size, kernel_size), sigmaX=sigma, sigmaY=sigma)
        ax2 = plt.subplot(1, 2, 2)
        ax2.imshow(resultImg, cmap='gray')
        ax2.set_title("Result image")
        plt.draw()
kernel_slider.on_changed(updateKernel)

def updateSigma(val):
    global resultImg
    global firstAction
    global currentFunc
    global img
    global sigma
    global kernel_size
    if firstAction is True:
        plt.cla()
    else:
        firstAction = True
    if currentFunc == 4:
        sigma = val
        resultImg = cv.GaussianBlur(img, ksize=(kernel_size, kernel_size), sigmaX=sigma, sigmaY=sigma)
        ax2 = plt.subplot(1, 2, 2)
        ax2.imshow(resultImg, cmap='gray')
        ax2.set_title("Result image")
        plt.draw()
kernel_slider.on_changed(updateKernel)

plt.show()