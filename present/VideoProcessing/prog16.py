import numpy as np
import cv2 as cv
import scipy.ndimage as ndi

def nothing(x):
	pass

WINDOW_NAME = "Distance Transform"
cv.namedWindow(WINDOW_NAME)
cv.createTrackbar('Sigma', WINDOW_NAME, 1, 10, nothing)
cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FRAME_WIDTH, 256)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 144)

if not cap.isOpened():
	print("Cannot open camera...")
	exit()

while True:
	ret, frame = cap.read()

	if not ret:
		print("Can't receive frame... \nExiting...")
		break

	n1 = cv.getTrackbarPos('Sigma', WINDOW_NAME)
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	output = ndi.grey_erosion(gray, size=(7, 7), structure=np.ones((n1, n1)))

	cv.imshow(WINDOW_NAME, output)
	if cv.waitKey(1) == 27:
		break

cap.release()
cv.destroyAllWindows()
