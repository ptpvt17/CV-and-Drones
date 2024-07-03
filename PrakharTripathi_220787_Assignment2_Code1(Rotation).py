import cv2
import numpy as np

rotated_0_deg = None
rotated_90_deg = None
rotated_180_deg = None
rotated_270_deg = None

def rotate(img, angle):
    height, width = img.shape[:2]

    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

    cv2.imshow('rotated_img',rotated_img)
    cv2.waitKey(0)

def rotatedFlags():
    global rotated_0_deg, rotated_90_deg, rotated_180_deg, rotated_270_deg

    original_flag = cv2.imread('C:/Users/prakh/IndianFlag.png') 
    rotated_0_deg = original_flag
    rotated_90_deg = rotate(original_flag, 90)
    rotated_180_deg = rotate(original_flag, 180)
    rotated_270_deg = rotate(original_flag, 270)

rotatedFlags()


