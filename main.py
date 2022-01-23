import cv2
from steganographie import *


image_path = "/Users/kwentine/Pictures/shirohige_family.jpeg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
text = "hello world"

stenographied_image = steganography_image(image, text)
# cv2.imshow("stenographied_image", stenographied_image)
# cv2.waitKey(0)

print(get_text_from_steganographied_image(stenographied_image))
