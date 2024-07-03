import cv2
import numpy as np

def find_contours_of_color(image_path, target_color_lower, target_color_upper):

    image = cv2.imread(image_path)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, target_color_lower, target_color_upper)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    result_image = image.copy()
    cv2.drawContours(result_image, contours, -1, (0, 255, 0), 2)

    cv2.imshow('Original Image', image)
    cv2.imshow('Contours Around Target Color', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()