import numpy as np
import cv2 as cv
import scipy.ndimage as ndi

cap = cv.VideoCapture(0)
n = 5
k = np.ones((n, n, n), np.uint8)/(n*n*n)

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

	output = ndi.convolve(frame, k, mode='nearest')

	cv.imshow('Convolved frame', output)
	if cv.waitKey(1) == 27:
		break

cap.release()
cv.destroyAllWindows()
