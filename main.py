import cv2
import matplotlib.pyplot as plt
import numpy as np
import imutils
import easyocr

# READ IMAGE AND CONVERT TO GRAYSCALE AND THEN BLUR ----------------------
image = cv2.imread("images/self2.jpg")
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(grayscale_image, cmap='gray')
plt.title('Grayscale image')
# plt.axis('off')
plt.show()

# adaptive_threshold = cv2.adaptiveThreshold(grayscale_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# edged_image = cv2.Canny(adaptive_threshold, 30, 200)

bilateral_filter = cv2.bilateralFilter(grayscale_image, 11, 17, 17)
edged_image = cv2.Canny(bilateral_filter, 30, 200)
plt.imshow(cv2.cvtColor(edged_image, cv2.COLOR_BGR2RGB))
plt.title('Image after canny edge detection')
plt.show()

# FINDING CONTOUR COORDINATES TO DETECT NUMBERPLATE --------------------------
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
    
# print(location)

mask =np.zeros(grayscale_image.shape, np.uint8)
new_image = cv2.drawContours(mask, [location], 0, 255, -1)
new_image = cv2.bitwise_and(image, image, mask=mask)
plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))
plt.title('Masked image')
plt.show()

(x,y) = np.where(mask==255)
(x1,y1)= (np.min(x), np.min(y))
(x2,y2) = (np.max(x), np.max(y))
cropped_image = grayscale_image[x1:x2+1, y1:y2+1]
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.title('Cropped image')
plt.show()

# USING OCR READER TO READ TEXT FROM CROPPED IMAGE ------------------------
reader = easyocr.Reader(['en'])
result = reader.readtext(cropped_image)

# print(result)

# PRINTING NUMBERPLATE RESULT  -------------------------------
text = result[0][-2]
font = cv2.FONT_HERSHEY_SIMPLEX
final_text = cv2.putText(image, text=text, org=(approx[0][0][0], approx[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
final_text = cv2.rectangle(image, tuple(approx[0][0]), tuple(approx[2][0]), (255,0,0),3)
plt.imshow(cv2.cvtColor(final_text, cv2.COLOR_BGR2RGB))
plt.title('Final image with license plate detection')
plt.show()
print('License Plate:', text)
