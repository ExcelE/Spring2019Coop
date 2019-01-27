import cv2
import numpy as np

image_input = cv2.imread("pcb_image.jpg")
orig = cv2.imread("pcb_image.jpg")

image_output = cv2.cvtColor(image_input, cv2.COLOR_BGR2HSV)

print("Hello OpenCV")
print(image_output.shape[1])

scaling_factor = 4
image_output = cv2.resize(image_output,None,fx=0.4,fy=0.4)
orig = cv2.resize(orig,None,fx=0.4,fy=0.4)

#HSV band filter

hsv_low = np.array([0, 30, 60])
hsv_high = np.array([179, 40, 255])

mask = cv2.inRange(image_output, hsv_low, hsv_high)

#Erosion
kernel = np.ones((8,8),np.uint8)
# The first parameter is the original image, 
# kernel is the matrix with which image is  
# convolved and third parameter is the number  
# of iterations, which will determine how much  
# you want to erode/dilate a given image.  
mask = cv2.erode(mask, kernel, iterations=1) 
mask = cv2.dilate(mask, kernel, iterations=4)


#check

res = cv2.bitwise_and(orig, orig, mask=mask)


cv2.imshow('image', res)
cv2.imwrite('image_output.png',image_output)
cv2.waitKey(0)
cv2.destroyAllWindows()