import cv2
import numpy as np

correct_colors = {
    'orange': [255, 165, 0],
    'white': [255, 255, 255],
    'green': [0, 128, 0],
    'blue': [0, 0, 255],
    'black': [0, 0, 0]
}

def unskew(s):

    distorted_image = cv2.imread(s)

    height, width, _ = distorted_image.shape

    midline_colors = [distorted_image[i, 299] for i in range(height)]

    vertical = list(set(tuple(color) for color in midline_colors) - set([tuple(correct_colors['blue']), tuple(correct_colors['black'])]))

    color_mapping = dict(zip(vertical, ['orange', 'white', 'green']))

    for i in range(height):
        for j in range(width):
            pixel_color = tuple(distorted_image[i, j])
            if pixel_color in color_mapping:
                distorted_image[i, j] = np.array(correct_colors[color_mapping[pixel_color]])

    gray = cv2.cvtColor(distorted_image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)

    angle = np.mean([line[0][1] for line in lines])

    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle * 180 / np.pi, 1)
    unskewed_image = cv2.warpAffine(distorted_image, rotation_matrix, (width, height), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))

    cv2.imshow('Unskewed Reference Image', unskewed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

unskew(r'C:\Users\prakh\Testcase.jpg')