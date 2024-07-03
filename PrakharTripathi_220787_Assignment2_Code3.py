import cv2
import cv2.aruco as aruco
import numpy as np

def markers(s, dict_type):
    image = cv2.imread(s)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    aruco_dict = aruco.Dictionary_get(dict_type)

    parameters = aruco.DetectorParameters_create()

    corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    if ids is not None and len(ids) > 0:
        for i in range(len(ids)):
            image = aruco.drawDetectedMarkers(image, corners, ids)

            rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners[i], 1, np.eye(3), np.zeros((1, 4)))

            translation_vector = tvec[0][0]
            rotation_vector = rvec[0][0]

            xc, yc = np.mean(corners[i][0], axis=0)
            print(xc,yc)

            axis_length = 1.0
            m = np.eye(3)
            image = cv2.drawFrameAxes(image, cameraMatrix=m, distCoeffs=None, rvec=rotation_vector, tvec=translation_vector,
                                      length=axis_length)

        cv2.namedWindow("ArUco Marker Detection", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("ArUco Marker Detection", 800, 600)
        cv2.imshow("ArUco Marker Detection", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print(f"No ArUco markers detected in the given image for dictionary type {dict_type}.")

s = r'C:\Users\prakh\OneDrive\Pictures\Camera Roll\arucomarker.jpg'
dictionary_types = [aruco.DICT_6X6_250, aruco.DICT_7X7_100, aruco.DICT_ARUCO_ORIGINAL]

for dict_type in dictionary_types:
    markers(s, dict_type)
