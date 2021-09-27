# We need to install opencv using command "pip install opencv-python"
import cv2

# Reading the image
image = cv2.imread("three.jpg")
cv2.imshow("Given Picture", image)
cv2.waitKey(0)

# Converting it into grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Step1 : GrayScale", gray_image)
cv2.waitKey(0)

# Inverting the image
inverted_image = 255 - gray_image
cv2.imshow("Step 2: Invert", inverted_image)
cv2.waitKey(0)

# The pencil sketch
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imshow("Step3: Sketch", pencil_sketch)
cv2.waitKey(0)

# Final image
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)
