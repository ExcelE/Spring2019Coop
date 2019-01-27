#!/bin/bash

ORIGINAL_FILES=*.txt

for f in $ORIGINAL_FILES
do
    if ["$(wc -l $f)" -eq 0]; then
        echo Removed $f since empty
        rm $f
    elif [ "$(wc -l $f)" -le 10 ]; then 
        echo Less than 10: $f
        mv {,short_}$f
    elif [ "$(wc -l $f)" -ge 10 -a "$(wc -l $f)" -le 20 ]; then 
        echo Between 10 and 20: $f
        mv {,medium_}$f
    elif [ "$(wc -l $f)" -ge 20 ]; then 
        echo Greater than 20: $f
        mv {,long_}$f
    fi
done
