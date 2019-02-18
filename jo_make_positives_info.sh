#!/bin/bash

for positives in `find ./positive_images \( -name *.jpg -o -name *.png \)`;do echo $positives 1 0 0 110 110;done;
