import cv2
import numpy as np

def Sobel(s, resize_factor=1.0):
    img = cv2.imread(s, cv2.IMREAD_COLOR)

    img = cv2.resize(img, None, fx=resize_factor, fy=resize_factor)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    magnitude = np.sqrt(sobelx**2 + sobely**2)

    magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
    magnitude = np.uint8(magnitude)

    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
    cv2.imshow('Edge-Detected Image', magnitude)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = r'C:\Users\prakh\Downloads\Emma.jpg'
Sobel(image_path, resize_factor=0.6)