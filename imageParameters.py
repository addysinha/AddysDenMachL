import cv2

# Read Image File
sourceImg = cv2.imread("C:/Users/Abhyudaya sinha/Pictures/Sweetheart.jpeg")

print("Type of Parameter (sourceImage): {}".format(type(sourceImg)))
print("Height (Rows) of Image (sourceImage): {}".format(len(sourceImg)))
print("Width of (columns) of Image (sourceImage): {}".format(len(sourceImg[0])))
print("Channel of the Image (sourceImage): {}".format(len(sourceImg[0][0])))
print("Height, Width and Channel of the Image (sourceImage): {}".format(sourceImg.shape))
print("dType of the Image (sourceImage): {}".format(sourceImg.dtype))
print("Size (Number of pixel) of the Image (sourceImage): {}".format(sourceImg.size))

# Create a window with Name "OpenedImage"
cv2.namedWindow("SourceImage", 0)

# In the above created "OpenedImage" window, show the read image
cv2.imshow("SourceImage", sourceImg)

# Display the window for said milli-seconds (0 - indefinite till user exists, >=1 Milli - Seconds
cv2.waitKey(0)
cv2.destroyAllWindows()
