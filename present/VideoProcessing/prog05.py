import numpy as np
import cv2 as cv
import scipy.ndimage as ndi

def nothing(x):
	pass

WINDOW_NAME = "Live Convolution"
cv.namedWindow(WINDOW_NAME)
cv.createTrackbar('Kernel Size', WINDOW_NAME, 1, 5, nothing)
cap = cv.VideoCapture(0)
n = 1

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

	n = cv.getTrackbarPos('Kernel Size', WINDOW_NAME)
	k = np.ones((n, n, n), np.uint8)/(n*n*n)
	output = ndi.convolve(frame, k, mode='nearest')

	cv.imshow(WINDOW_NAME, output)
	if cv.waitKey(1) == 27:
		break

cap.release()
cv.destroyAllWindows()
