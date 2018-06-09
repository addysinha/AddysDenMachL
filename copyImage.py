import cv2

# Read Image File
sourceImg = cv2.imread("C:/Users/Abhyudaya sinha/Pictures/Addys_Photography/File_008.jpeg")

# Copy the image to create destImage
cv2.imwrite("C:/Users/Abhyudaya sinha/Pictures/Addys_Photography/File_008_duplicate.jpeg", sourceImg)

# Read copied image in destImg
destImg = cv2.imread("File_008_duplicate.jpeg")

# Create a window with Name "OpenedImage"
cv2.namedWindow("CopiedImage", 0)

# In the above created "OpenedImage" window, show the read image
cv2.imshow("CopiedImage", destImg)

# Display the window for said milli-seconds (0 - indefinite till user exists, >=1 Milli - Seconds
cv2.waitKey(0)
