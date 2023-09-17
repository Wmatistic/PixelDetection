import cv2
import numpy as np
import imutils

image = cv2.imread("pixelSample4.png");

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
blurred = cv2.GaussianBlur(image_hsv, (5,5), 0)
thresh = cv2.threshold(blurred, 160, 255, cv2.THRESH_BINARY)[1]


# define white color range in HSV
white_sensitivity = 60
white_lower_bound = np.array([0, 0, 255-white_sensitivity])
white_upper_bound = np.array([255, white_sensitivity, 255])

# apply white color range to HSV image to create mask
mask = cv2.inRange(thresh, white_lower_bound, white_upper_bound)
#invert mask
inverted_mask = 255-mask

# removing noise from mask
kernel = np.ones((7,7), np.uint8)

mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# segment the detected pixels from original image
segmented_image = cv2.bitwise_and(image, image, mask=mask)
#segmented_image = cv2.bitwise_and(segmented_image, segmented_image, mask=inverted_mask)

# find contours from mask
contours = cv2.findContours(mask.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

# draw boundary around detected pixels
#output = cv2.drawContours(image, contours, -1, (0, 0, 255), 2)
output = image

# draw text and circles on the detected pixels
for c in contours:

    approx = cv2.approxPolyDP(c, 0.05 * cv2.arcLength(c, True), True)

    M = cv2.moments(c)
    if M["m00"] != 0.0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

    if len(approx) == 6:
        cv2.circle(image, (cX, cY), 7, (255, 0, 255), -1)
        cv2.putText(output,"WHITE !!", (cX, cY),
        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

cv2.imshow("Mask", segmented_image)
cv2.imshow("Pixels", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
