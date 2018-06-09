import numpy as np
import cv2

rgbImage = cv2.imread("C:/Users/Abhyudaya sinha/Pictures/Sweetheart.jpeg", 1)
grayImage = cv2.cvtColor(rgbImage, cv2.COLOR_RGB2GRAY)

cv2.imshow("rgbImage", rgbImage)
cv2.imshow("grayImage", grayImage)

cv2.waitKey(0)
cv2.destroyAllWindows()



