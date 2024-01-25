
import time

import cv2
import skimage                 # form 1, load whole skimage library
import skimage.io              # form 2, load skimage.io module only
import imageio
from skimage.io import imread   # form 3, load only the imread function
import numpy as np             # form 4, load all of numpy into an object called np
import matplotlib as plt

img_analyser = imageio.imread('plus.PNG')
img_sample = imageio.imread('test.jpg')
'''while True:
    image = skimage.io.imread(fname="test.jpg")
    print(image)
    cv2.imshow('secret', image)

   '''


