import cv2  # import thư viện OpenCV
import numpy as np #import thư viện numpy để làm việc với dữ liệu kiểu mảng
import matplotlib.pyplot as plt # import thư viện matplotlib để vẽ ảnh
def display():
	print('---KHOI PHUC ANH TRONG MIEN SO HOC---')
	arr=['• Trung bình số học',
	'• Trung bình Contraharmonic',
	'• Lọc trung vị',
    '• Lọc Max, Min',
    '• Lọc Midpoint'
	]
	for i,val in enumerate(arr):
		print(i+1," ",val)
#goi ham
display()
# Nhap so vao
x = int(input("Select: "))
# Viet cac ham xu ly
def 0_Trung_Binh_So_Hoc():
	print('Sunday Fuction')
# switch case cho cac so
def select_function(i):
        switcher={
                0:Sunday(),
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'Saturday',
                7:lambda:print('lambda')
             }
        func = switcher.get(i,lambda :'Invalid')
        return func

select_function(x)