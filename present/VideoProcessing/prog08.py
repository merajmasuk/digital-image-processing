import numpy as np
import cv2 as cv
import scipy.ndimage as ndi

def nothing(x):
	pass

WINDOW_NAME = "Live Uniform"
cv.namedWindow(WINDOW_NAME)
cv.createTrackbar('Filter Size', WINDOW_NAME, 1, 15, nothing)
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

	n = cv.getTrackbarPos('Filter Size', WINDOW_NAME)
	output = ndi.uniform_filter(frame, size=n)

	cv.imshow(WINDOW_NAME, output)
	if cv.waitKey(1) == 27:
		break

cap.release()
cv.destroyAllWindows()
