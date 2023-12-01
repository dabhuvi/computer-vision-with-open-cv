import cv2
import numpy as np
def sharpen_image(image, boost_factor):
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    mask = image - blurred
    sharpened = image + boost_factor * mask
    sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)
    return sharpened
input_image = cv2.imread("C:/Users/logetha/Downloads/luffy.jpg")
boost_factor = 1.5
sharpened_image = sharpen_image(input_image, boost_factor)
cv2.imshow('Original Image', input_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
