import cv2
import numpy as np

def ig_filter(image_path):
    image = cv2.imread(image_path)

    brightness_factor = 0.5
    image = cv2.convertScaleAbs(image, alpha=brightness_factor)

    contrast_factor = 1.5
    image = cv2.convertScaleAbs(image, alpha=contrast_factor)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    saturation_factor = 1.5
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * saturation_factor, 0, 255)

    filtered_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    return filtered_image