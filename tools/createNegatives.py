#!/usr/bin/env python
# import the necessary packages
import argparse
import numpy as np
import cv2
# Import system lib (filename as parameter)
import sys, os
# file/directory path manipulation
from os.path import basename, dirname

destination="/home/jody/opencv-haar-classifier-training/negative_images_loop/"

# construct the argument parse and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True,
	help="path to the input image")
parser.add_argument('--width', nargs='?', const=110, type=int, default=110,
	help="Width zone")
parser.add_argument('--height', nargs='?', const=110, type=int, default=110,
        help="height zone")

args = vars(parser.parse_args())

print(args);

print(args["width"], args["height"])
def newImageName(args, destination_dir=destination):
	image = args["image"]
	base = os.path.basename(image)
	print(os.path.splitext(base))
	filename  = os.path.splitext(base)[0]
	zone = '_' + str(args["xpos"]) + 'x' + str(args["ypos"])
	extension = os.path.splitext(base)[1]
	#newImageName = destination_dir + '/' + base
	newImageName = destination_dir + '/' + filename + zone + extension
	print("newImageName", newImageName)
	return newImageName


image = cv2.imread(args["image"])
height, width, channels = image.shape

#args["ypos"]=0
#y=args["ypos"]
#x=args["xpos"]
h=args["height"]
w=args["width"]

croped_by_width = width / w
croped_by_height = height / h
ypos = 0
xpos = 0
args["ypos"] = ypos
args["xpos"] = xpos

for y in xrange(croped_by_height): 
    for x in xrange(croped_by_width):
            print("xpos", args["xpos"], "ypos", args["ypos"])
            crop = image[args["ypos"]:args["ypos"]+h, args["xpos"]:args["xpos"]+w]
            destImgName = newImageName(args)
            args["xpos"] = args["xpos"] + w
            cv2.imwrite(destImgName, crop)
            cv2.imshow('Image', crop)
    args["ypos"] = args["ypos"] + h
    args["xpos"] = 0
#cv2.waitKey(0)


