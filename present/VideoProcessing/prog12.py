import numpy as np
import cv2 as cv
import scipy.ndimage as ndi

def nothing(x):
	pass

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

	o1 = ndi.prewitt(frame)
	o2 = ndi.laplace(frame)

	cv.imshow("Prewitt", o1)
	cv.imshow("Laplace", o2)
	if cv.waitKey(1) == 27:
		break

cap.release()
cv.destroyAllWindows()
