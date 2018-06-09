import cv2
import numpy as np

# Zeros represent Black
black = np.zeros([300, 200, 1], 'uint8')
cv2.imshow("Black Window", black)
print(black[0,0,:])

# Ones represent transition to white, but as the value is 1, so its close to Black
almostBlack = np.ones([300, 200, 3], 'uint8')
cv2.imshow("Almost Black Window", almostBlack)
print(almostBlack[0,0,:])

# Ones represent transition to white, and as the value is 255 (max) - (2**16 - 1), so its color is 255
white = np.ones([300, 200, 3], 'uint8') * 255
cv2.imshow("White Window", white)
print(white[0,0,:])

# Ones represent transition to white, but as the value is (255, 0, 0) i.e. (B, G, R), so the color is Blue
blue = np.ones([300, 200, 3], 'uint8')
blue[:,:] = (255,0,0)
cv2.imshow("Blue Window", blue)
print(blue[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()