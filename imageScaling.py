import cv2
import numpy as np

origImage = cv2.imread("C:/Users/Abhyudaya sinha/Pictures/Sweetheart.jpeg")
cv2.imshow("Original Image", origImage)

halfImage = cv2.resize(origImage, (0,0), fx=0.5, fy=0.5)
cv2.imshow("Half Image", halfImage)

strechImage = cv2.resize(origImage, (200, 200))
cv2.imshow("Strech Image", strechImage)

strechNearImage = cv2.resize(origImage, (200, 200), interpolation=cv2.INTER_NEAREST)
cv2.imshow("Strech Near Image", strechNearImage)

cv2.waitKey(0)
cv2.destroyAllWindows()