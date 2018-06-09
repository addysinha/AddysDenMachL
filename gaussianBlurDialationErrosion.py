import cv2
import numpy as np

origImage = cv2.imread("C:/Users/Abhyudaya sinha/Pictures/Sweetheart.jpeg", 1)
cv2.imshow("Original Image", origImage)

gaussianBlur = cv2.GaussianBlur(origImage, (5, 55), 0)
cv2.imshow("Gaussian Blur Image", gaussianBlur)

# Gaussian Blur
gaussianBlur = cv2.GaussianBlur(origImage, (5, 55), 0)
cv2.imshow("Gaussian Blur Image", gaussianBlur)

#Dilation and Erosion
kernel = np.ones((5, 5), 'uint8')

dialationImage = cv2.dilate(origImage, kernel, iterations=1)
erosionImage = cv2.erode(origImage, kernel, iterations=1)

cv2.imshow("Dialation Image", dialationImage)
cv2.imshow("Errosion Image", erosionImage)

cv2.waitKey(0)
cv2.destroyAllWindows()