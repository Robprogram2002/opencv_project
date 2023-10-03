import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('cat image', img)
cv.waitKey(0)


