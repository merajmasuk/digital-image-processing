import numpy as np
import cv2 as cv
from datetime import datetime

cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FRAME_WIDTH, 256)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 144)

if not cap.isOpened():
	print("Cannot open camera...")
	exit()

while True:
	ret, frame = cap.read()

	if not ret:
		print("Can't receive frame...\nExiting...")
		break

	print(datetime.now())

	print(frame.dtype)
	print(frame.shape)
	print(frame.ndim)
	print(frame.size)

	b = frame[:, :, 0]
	g = frame[:, :, 1]
	r = frame[:, :, 2]

	cv.imshow('Red', r)
	cv.imshow('Green', g)
	cv.imshow('Blue', b)
	if cv.waitKey(1) == 27:
		break

cap.release()
cv.destroyAllWindows()
