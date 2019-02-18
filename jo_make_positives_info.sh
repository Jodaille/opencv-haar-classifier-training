#!/bin/bash

for positives in `find ./positive_images -iname "*.*"`;do echo $positives 1 0 0 110 110;done;
