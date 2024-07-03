import cv2
import numpy as np
from matplotlib import pyplot as plt

def rectangular_low_pass_filter(size, cutoff_frequency):
    rows = np.fft.fftfreq(size[0])
    cols = np.fft.fftfreq(size[1])
    filter_rows = np.abs(rows) <= cutoff_frequency
    filter_cols = np.abs(cols) <= cutoff_frequency
    lp_filter = np.outer(filter_rows, filter_cols)
    return lp_filter.astype(float)

def hybrid(s1, s2):
    img1 = cv2.imread(s1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(s2, cv2.IMREAD_GRAYSCALE)

    img1 = cv2.resize(img1, (256, 256))
    img2 = cv2.resize(img2, (256, 256))

    f1 = np.fft.fft2(img1)
    f2 = np.fft.fft2(img2)

    filter_size = (256, 256)
    cutoff_frequency = 0.1  
    lp_filter = rectangular_low_pass_filter(filter_size, cutoff_frequency)

    f1_lp = f1 * lp_filter
    f2_lp = f2 * lp_filter

    img1_lp = np.abs(np.fft.ifft2(f1_lp)).astype(np.uint8)
    img2_lp = np.abs(np.fft.ifft2(f2_lp)).astype(np.uint8)

    hybrid_img = (img1_lp + img2_lp) // 2

    plt.figure(figsize=(10, 10))

    plt.subplot(2, 3, 1)
    plt.imshow(lp_filter, cmap='gray')
    plt.title('1) Rectangular Low Pass Filter')

    plt.subplot(2, 3, 2)
    plt.imshow(np.log(1 + np.abs(f1)), cmap='gray')
    plt.title('2) Fourier of Image 1')

    plt.subplot(2, 3, 3)
    plt.imshow(np.log(1 + np.abs(f1_lp)), cmap='gray')
    plt.title('3) Fourier after Low Pass Filter')

    plt.subplot(2, 3, 4)
    plt.imshow(np.log(1 + np.abs(f2)), cmap='gray')
    plt.title('4) Fourier of Image 2')

    plt.subplot(2, 3, 5)
    plt.imshow(np.log(1 + np.abs(f2_lp)), cmap='gray')
    plt.title('5) Fourier after Low Pass Filter (Image 2)')

    plt.subplot(2, 3, 6)
    plt.imshow(hybrid_img, cmap='gray')
    plt.title('6) Combined Hybrid Image')

    plt.show()
    cv2.imshow('Image 1',img1)
    cv2.imshow('Image 2',img2)
    cv2.imshow('Modified Image 1 (Low Pass)', img1_lp)
    cv2.imshow('Modified Image 2 (Low Pass)', img2_lp)
    cv2.imshow('Combined Hybrid Image', hybrid_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

image1_path = r'C:\Users\prakh\Downloads\Einstein.jpg'
image2_path = r'C:\Users\prakh\Downloads\opp.jpg'
hybrid(image1_path, image2_path)