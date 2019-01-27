#!/bin/bash

ORIGINAL_FILES=*.txt

for f in $ORIGINAL_FILES
do
    FILE_SIZE="$(wc -l < $f)"
    if [ $FILE_SIZE -eq 0 ]; then
        echo Removed $f since empty
        rm $f
    elif [ $FILE_SIZE -le 10 -a $FILE_SIZE -gt 0 ]; then 
        echo Less than 10: $f
        mv {,short_}$f
    elif [ $FILE_SIZE -ge 10 -a $FILE_SIZE -le 20 ]; then 
        echo Between 10 and 20: $f
        mv {,medium_}$f
    elif [ $FILE_SIZE -ge 20 ]; then 
        echo Greater than 20: $f
        mv {,long_}$f
    fi
done
