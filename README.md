# PixelDetection
This is a test program built using Python to detect the game elements, called Pixels, in the 2023 FTC game CENTERSTAGE.

## Explanation
The program initially blurs and creates a threshold of the original image allowing for colors to be easily defined. Then it creates a mask of the image using a upper and lower bound of the colors for the possible colors the pixels can appear as, additionally noise is removed from this mask. 
Next a segmented image is created for visual debugging purposes with bitwise and cv2 function. After this it draws contours around the pixels found in the mask. Something important to note in this step is that it's looking for contours **inside** the pixel to avoid contours branching between pixels.
After this it looks for contours with 6 sides, hexagons, inside the pixels and draws circles and text inside the contours.

## Detection Test Images
![image](https://github.com/Wmatistic/PixelDetection/assets/52674478/54abf2cf-b013-48b1-8532-28a8d1090535)

## [FTC Game Reveal / Animation](https://www.youtube.com/watch?v=lDcZCR4GOpY&t=4s&ab_channel=FirstUpdatesNow)
