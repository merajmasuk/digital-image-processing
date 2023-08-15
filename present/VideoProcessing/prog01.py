import numpy as np
import cv2 as cv

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

	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	cv.imshow('frame', frame)
	if cv.waitKey(1) == 27:
		break

cap.release()
cv.destroyAllWindows()
