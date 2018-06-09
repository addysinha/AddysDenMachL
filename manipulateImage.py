import cv2
import numpy as np

sourceImg = cv2.imread("C:/Users/Abhyudaya sinha/Pictures/Sweetheart.jpeg")
# Set Red (2) as 0 - i.e. Suppress Red color.
sourceImg[:, :, 2] = 0

print(sourceImg.item(sourceImg.shape[0]-1, sourceImg.shape[1]-2, 0))

cv2.imshow("Image", sourceImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
