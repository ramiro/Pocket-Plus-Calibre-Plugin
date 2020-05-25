#!/bin/zsh

every=5
N=$((60/$every))

while [ $N -ne 0 ]
do
    python /Users/magnus/workspace/Pocket-Plus-Calibre-Plugin/push/push-script.py \
           /Users/magnus/Library/Mobile\ Documents/iCloud~is~workflow~my~workflows/Documents \
           /Users/magnus/workspace/Pocket-Plus-Calibre-Plugin/push/push.sh # &> ~/Desktop/log.txt
      sleep $every
      ((N--))
      # echo $N
done
exit
