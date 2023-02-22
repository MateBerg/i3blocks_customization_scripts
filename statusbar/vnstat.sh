#!/bin/bash

#get the last line
IN=$(vnstat -d 1 -i wlan0 | (tail -n 3))
#convert to array
arrOUT=(${IN//|/ })
#format the output
OUTPUT="${arrOUT[5]} ${arrOUT[6]} "
#pick one
echo $OUTPUT