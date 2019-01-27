#!/bin/bash

ORIGINAL_FILES=*.txt

for f in $ORIGINAL_FILES
do
    FILE_SIZE="$(wc -l < $f)"
    if [ $FILE_SIZE -eq 0 ]; then
        echo Removed $f since empty
        rm $f
    elif [ $FILE_SIZE -lt 10 -a $FILE_SIZE -gt 0 ]; then 
        echo $f: Less than 10 \($FILE_SIZE lines\)
        mv {,short_}$f
    elif [ $FILE_SIZE -ge 10 -a $FILE_SIZE -le 20 ]; then 
        echo $f: Between 10 and 20 \($FILE_SIZE lines\)
        mv {,medium_}$f
    elif [ $FILE_SIZE -gt 20 ]; then 
        echo $f: Greater than 20 \($FILE_SIZE lines\)
        mv {,long_}$f
    fi
done
