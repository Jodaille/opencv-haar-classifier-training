#!/bin/bash

FILENAME=$1
NAME="${FILENAME%.*}"
EXTENSION="${FILENAME##*.}"
echo $NAME $EXTENSION
SUFFIX="_rotated."
NEWNAME="$NAME$SUFFIX$EXTENSION"

echo NEWNAME $NEWNAME

rotate_image () {
    FILENAME=$1
    ANGLE=$2
    NAME="${FILENAME%.*}"
    EXTENSION="${FILENAME##*.}"
    echo $NAME $EXTENSION
    SUFFIX="_rotated_$ANGLE."
    NEWNAME="$NAME$SUFFIX$EXTENSION"

    echo NEWNAME $NEWNAME
	if [ "$EXTENSION" = "jpg" ]; then
		  echo "FILE IS jpg"
	#         cp $FILENAME $NEWNAME
		  jpegtran -rotate $ANGLE $FILENAME > $NEWNAME
	fi

}

rotate_image $FILENAME 90
rotate_image $FILENAME 180
rotate_image $FILENAME 270

