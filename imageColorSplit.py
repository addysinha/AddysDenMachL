import numpy as np
import cv2

image = cv2.imread("C:/Users/Abhyudaya sinha/Pictures/Sweetheart.jpeg", 1)
cv2.imshow("Display Image", image)
cv2.moveWindow("Display Image", 0, 0)

height, width, channels = image.shape
print(f'height: {height}, width: {width}, channels: {channels}')

b, g, r = cv2.split(image)
print(f'red: {r}, green: {g}, blue: {b}')

rgb_split = np.empty([height, width*3, 3], 'uint8')

rgb_split[:,0:width] = cv2.merge([b, b, b])
rgb_split[:,width:width*2] = cv2.merge([g, g, g])
rgb_split[:,width*2:width*3] = cv2.merge([r, r, r])

cv2.imshow("RGBChannels", rgb_split)
cv2.moveWindow("RGBChannels", 0, 0)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow("HSVImage", hsv_image)
cv2.moveWindow("HSVImage", 0, 0)

h, s, v = cv2.split(hsv_image)
hsv_split = np.concatenate((h,s,v), axis=1)

cv2.imshow("HSVChannels", hsv_split)
cv2.moveWindow("HSVChannels", 0, 0)

cv2.waitKey(0)
cv2.destroyAllWindows()