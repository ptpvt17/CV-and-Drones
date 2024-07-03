import cv2
import numpy as np

def shape(input_image):

    image = cv2.imread(input_image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred_gray = cv2.GaussianBlur(gray, (5,5), 0)

    edges = cv2.Canny(blurred_gray, 30, 150)

    contours, _= cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        epsilon = 0.04*cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        vertices = len(approx)
        if vertices == 3:
            shape = "Triangle"
        elif vertices == 4:
            (x,y,w,h) = cv2.boundingRect(approx)
            ar = w/float(h)
            shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
        elif vertices == 5:
            shape = "Pentagon"    
        else:
            shape = "Circle"

        cv2.drawContours(image, [approx], 0, (0,255,0), 2)
        cv2.putText(image, shape, (approx[0][0][0], approx[0][0][1]+5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.imwrite('shapes_Detected.jpg', image)

    cv2.imshow('Detected Shapes',image)
    cv2.waitKey()
    cv2.destroyAllWindows()

