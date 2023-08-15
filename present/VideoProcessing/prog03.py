import numpy as np
import cv2 as cv
import scipy.ndimage as ndi

angle = 0
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

	angle = (angle+1) % 360
	output = ndi.rotate(frame, angle, reshape=False)

	cv.imshow('Rotated frame', output)
	if cv.waitKey(1) == 27:
		break

cap.release()
cv.destroyAllWindows()
