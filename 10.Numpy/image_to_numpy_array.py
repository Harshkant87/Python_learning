import numpy
import cv2

im_g = cv2.imread("OIP.jpg", 0)
print(im_g)
print(im_g.shape)

# you can also slice this two dimensional array
# 1. stacking of these arrays:
im_g_stack = numpy.hstack((im_g, im_g)) #horizontal stacking
print(im_g_stack)
print(im_g_stack.shape)

im_g_stack = numpy.vstack((im_g, im_g)) #vertical stacking
print(im_g_stack)
print(im_g_stack.shape)

# 2. Splitting of arrays
im_g_split = numpy.hsplit(im_g, 3) #horizontal split
print(im_g_split)



