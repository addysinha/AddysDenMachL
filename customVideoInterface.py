import cv2

videoCapture = cv2.VideoCapture(0)

color = (255, 0, 0) #Blue Color
line_width = 3
radius = 100
point = (0, 0)

def click(event, x, y, flags, param):
    global point, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'Pressed: {x},{y}')
        point = (x, y)

cv2.namedWindow("CustomInterfaceVideo")
cv2.setMouseCallback("CustomInterfaceVideo", click)

while(True):
    ret, frame = videoCapture.read()
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    cv2.circle(frame, point, radius, color, line_width)

    cv2.imshow("CustomInterfaceVideo", frame)

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

