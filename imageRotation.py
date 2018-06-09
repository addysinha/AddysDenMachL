import cv2
import numpy as np

origImage = cv2.imread("C:/Users/Abhyudaya sinha/Pictures/Sweetheart.jpeg", 1)
cv2.imshow("Original Image", origImage)

angle = cv2.getRotationMatrix2D((0,0), -30, 1)
rotatedImage = cv2.warpAffine(origImage, angle, (origImage.shape[1], origImage.shape[0]))
cv2.imshow("Rotated Image", rotatedImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
