import cv2
import numpy as np

def hough_line(image_path):

    original_image = cv2.imread(image_path)

    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray_image, 50, 150, apertureSize=3)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            cv2.line(original_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow('Original Image', cv2.imread(image_path))
    cv2.imshow('Superposed Lines', original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()