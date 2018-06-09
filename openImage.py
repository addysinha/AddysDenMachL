import cv2

# Read Image File
img = cv2.imread("C:/Users/Abhyudaya sinha/Pictures/Addys_Photography/File_008.jpeg")

# Create a window with Name "OpenedImage"
cv2.namedWindow("OpenedImage", 0)

# In the above created "OpenedImage" window, show the read image
cv2.imshow("OpenedImage", img)

# Display the window for said milli-seconds (0 - indefinite till user exists, >=1 Milli - Seconds
cv2.waitKey(0)
