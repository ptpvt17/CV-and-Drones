import cv2

def solve(s):
    image = cv2.imread(s)

    edges = cv2.Canny(image, 50, 150)  

    cv2.imshow('Original Image', image)
    cv2.imshow('Canny Edge Detection', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image=r'C:\Users\prakh\Downloads\images.png'
solve(image)