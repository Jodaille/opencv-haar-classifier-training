#!/usr/bin/env python
# import the necessary packages
import argparse
import numpy as np
import cv2
# Import system lib (filename as parameter)
import sys, os
# file/directory path manipulation
from os.path import basename, dirname

destination="/home/jody/opencv-haar-classifier-training/positive_images/"

# construct the argument parse and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True,
	help="path to the input image")
parser.add_argument("-x", "--xpos", required=True,type=int,
        help="path to the input image")
parser.add_argument("-y", "--ypos", required=True,type=int,
        help="path to the input image")
parser.add_argument('--width', nargs='?', const=110, type=int, default=110,
	help="Width zone")
parser.add_argument('--height', nargs='?', const=110, type=int, default=110,
        help="height zone")

args = vars(parser.parse_args())

print(args);

print(args["width"], args["height"])
def newImageName(image, destination_dir=destination):
	base = os.path.basename(image)
	filename = os.path.splitext(base)[0]
	newImageName = destination_dir + '/' + base
	print("newImageName", newImageName)
	return newImageName

destImgName = newImageName(args["image"])

image = cv2.imread(args["image"])
y=args["ypos"]
x=args["xpos"]
h=args["height"]
w=args["width"]
crop = image[y:y+h, x:x+w]
cv2.imwrite(destImgName, crop)
cv2.imshow('Image', crop)

cv2.waitKey(0)


