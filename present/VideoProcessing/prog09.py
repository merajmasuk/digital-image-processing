import numpy as np
import cv2 as cv
import scipy.ndimage as ndi

def nothing(x):
	pass

WINDOW_NAME = "Live Percentile"
cv.namedWindow(WINDOW_NAME)
cv.createTrackbar('Size', WINDOW_NAME, 1, 5, nothing)
cv.createTrackbar('Percentile', WINDOW_NAME, 1, 75, nothing)
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

	s = cv.getTrackbarPos('Size', WINDOW_NAME)
	p = cv.getTrackbarPos('Percentile', WINDOW_NAME)
	output = ndi.percentile_filter(frame, size=s, percentile=p)

	cv.imshow(WINDOW_NAME, output)
	if cv.waitKey(1) == 27:
		break

cap.release()
cv.destroyAllWindows()
