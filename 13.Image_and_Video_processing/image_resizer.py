import cv2

img = cv2.imread("galaxy.jpg", 1)
print(img.shape)

resized_image = cv2.resize(img, (1000, 500)) # resizing the resolution of image
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized_image.jpg", resized_image)
cv2.waitKey(0) # you can put miliseconds value here as well, 0 means any pressed key will close the window
cv2.destroyAllWindows()