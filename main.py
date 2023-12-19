import cv2
import matplotlib.pyplot as plt
import numpy as np
import imutils
import easyocr

# READ IMAGE AND CONVERT TO GRAYSCALE AND THEN BLUR ----------------------
image = cv2.imread('images/car2.jpg')
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(grayscale_image, cmap='gray')
# plt.axis('off')
plt.show()

bilateral_filter = cv2.bilateralFilter(grayscale_image, 11, 17, 17)
edged_image = cv2.Canny(bilateral_filter, 30, 200)
plt.imshow(cv2.cvtColor(edged_image, cv2.COLOR_BGR2RGB))
plt.show()

keypoints = cv2.findContours(edged_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

location = None
for contour in contours:
    # perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break
    
print(location)