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
mask = cv2.erode(mask,kernel, 1)
kernel = np.ones((8,8),np.uint8)
mask = cv2.dilate(mask,kernel, 1)


#check

res = cv2.bitwise_and(orig, orig, mask=mask)


cv2.imshow('image', res)
cv2.imwrite('image_output.png',image_output)
cv2.waitKey(0)
cv2.destroyAllWindows()