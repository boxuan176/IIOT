import cv2
import numpy as np

#gray
image = cv2.imread("TW.jpg")    #先讀取圖片
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #把image這個檔案從BGR轉成灰階，放到gray這個變數

#no function
image1 = cv2.imread("TW.jpg")
b = image1[:,:,0] 
g = image1[:,:,1]  
r = image1[:,:,2]  
gray_nofunc = 0.3*b + 0.3*g + 0.3*r
gray_nofunc = gray_nofunc.astype(np.uint8)

#threshold
ret,thresh1 = cv2.threshold(gray,245,255,cv2.THRESH_BINARY)

cv2.imwrite('image.jpg',image)
cv2.imwrite("gray.jpg", gray)
cv2.imwrite("gray_nofunc.jpg", gray_nofunc)
cv2.imwrite("threshold2.jpg", thresh1)
cv2.waitKey(0)             #等待 enter被按下
cv2.destroyAllWindows()    #關閉opencv開啟的視窗
