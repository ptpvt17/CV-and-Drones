import cv2
import numpy as np

def generate_flag():
    height, width = 600, 900
    flag = np.ones((height, width, 3), dtype=np.uint8) * 255 

    saffron = (0, 153, 255)   
    green = (7, 136, 18)     
    navy_blue = (128, 0, 0)  

    flag[:200, :] = saffron
    flag[400:, :] = green

    center_coordinates = (width // 2, height // 2)  
    radius = 100  
    thickness = 2 

    cv2.circle(flag, center_coordinates, radius, navy_blue, thickness)

    for i in range(0, 360, 15):
        x = int(center_coordinates[0] + radius * np.cos(np.radians(i)))
        y = int(center_coordinates[1] + radius * np.sin(np.radians(i)))
        cv2.line(flag, center_coordinates, (x, y), navy_blue, thickness)

    cv2.imshow('Indian Flag', flag)
    cv2.imwrite("C:/Users/prakh/IndianFlag.png",flag)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

generate_flag()
