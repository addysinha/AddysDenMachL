import cv2
import numpy as np

whiteImage = np.ones([500,500,3], 'uint8') * 255

point = (0,0)
radius = 0
color = (0,255,0) #Green Color
line_width = 5

def click(event, x, y, flags, param):
    global whiteImage, point
    if event == cv2.EVENT_MOUSEMOVE:
        print(f'Pressed: {x} {y}')
        point = (x, y)

cv2.namedWindow("DrawingApp")
cv2.setMouseCallback("DrawingApp", click)

while(True):
    cv2.circle(whiteImage, point, radius, color, line_width)
    cv2.imshow("DrawingApp", whiteImage)

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    if ch & 0xFF == ord('g'):
        color = (0, 255, 0)
    if ch & 0xFF == ord('b'):
        color = (255, 0, 0)
    if ch & 0xFF == ord('r'):
        color = (0, 0, 255)

cv2.destroyAllWindows()