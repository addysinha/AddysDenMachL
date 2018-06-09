import cv2
import numpy as np
import os

randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)

#print(f'randomByteArray:{os.urandom(120000)}')
#print(f'flatNumpyArray:{flatNumpyArray}')

# 200 * 600 = 120000
grayImg = flatNumpyArray.reshape(200, 600)
# 100 * 400 * 3 = 120000
bgrImg = flatNumpyArray.reshape(100, 400, 3)

cv2.imshow("Gray Image", grayImg)
cv2.imshow("BGR Image", bgrImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
