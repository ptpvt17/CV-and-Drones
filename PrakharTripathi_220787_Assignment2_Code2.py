import numpy as np
import cv2 as cv

chessboardSize = (6,6)

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.0001)


objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)

size_of_chessboard_squares_mm = 100
objp = objp * size_of_chessboard_squares_mm

objpoints = []  
imgpoints = []  


img = cv.imread(r'C:\Users\prakh\calib3.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    
ret, corners = cv.findChessboardCorners(gray, chessboardSize, criteria)

if ret == True:
    objpoints.append(objp)
    imgpoints.append(corners)
    ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    undistorted_img = cv.undistort(img, mtx, dist, None, mtx)

    cv.imshow('Undistorted Image', undistorted_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

