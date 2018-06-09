import cv2
import numpy as np

image = cv2.imread("C:/Users/Abhyudaya sinha/Pictures/Sweetheart.jpeg", 1)

b, g, r = cv2.split(image)

# Merge function processes the image - Passing b, g, r
# and 4th Parameter is the color which we want to make visible
processedGreenImage = cv2.merge((b, g, r, g))
cv2.imwrite("C:/Users/Abhyudaya sinha/Pictures/SweetheartGreenPNG.png", processedGreenImage)

processedRedImage = cv2.merge((b, g, r, r))
cv2.imwrite("C:/Users/Abhyudaya sinha/Pictures/SweetheartRedPNG.png", processedRedImage)

processedBlueImage = cv2.merge((b, g, r, b))
cv2.imwrite("C:/Users/Abhyudaya sinha/Pictures/SweetheartBluePNG.png", processedBlueImage)
