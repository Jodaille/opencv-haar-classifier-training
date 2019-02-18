
# project cleaning
rm samples/*.vec
rm classifier/*.xml
rm samples.vec

find ./positive_images -iname "*.jpg" > positives.txt
find ./negative_images -iname "*.jpg" > negatives.txt

perl bin/createsamples.pl positives.txt negatives.txt samples 1500 "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1 -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 110 -h 110"

python ./tools/mergevec.py -v samples/ -o samples.vec

opencv_traincascade -data classifier -vec samples.vec -bg negatives.txt   -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 1000 -numNeg 600 -w 110 -h 110 -mode ALL -precalcValBufSize 1024   -precalcIdxBufSize 1024 -featureType LBP

opencv_traincascade -data classifier -vec samples.vec -bg negatives.txt   -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 1000 -numNeg 600 -w 24 -h 20  -mode ALL -precalcValBufSize 1024   -precalcIdxBufSize 1024 -featureType LBP

# cf: https://www.youtube.com/watch?v=WEzm7L5zoZE

./jo_make_positives_info.sh  > vv.info
# -num = number of positives images
opencv_createsamples -info vv.info -num 51 -w 20 -h 20 -vec vv.vec

opencv_traincascade -data classifier -vec vv.vec -bg negatives.txt -numPos 51 -numNeg 851 -numStages 20 -w 20 -h 20 -featureType LBP


