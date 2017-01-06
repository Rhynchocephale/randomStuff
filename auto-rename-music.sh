#! /bin/bash

declare -A id3tags
#typeset -A id3tags
id3tags["TITLE"]="TIT2"
id3tags["ALBUM"]="TALB"
#id3tags[YEAR]="TYER"
id3tags["TRACK"]="TRCK"

#for SONG in `find "$1" -type f -name "*mp3"`
find "$1" -type f -name "*.mp3" -print0 | while IFS= read -r -d '' SONG
do
  echo "Processing $SONG !"
  rm -f /tmp/song_tags /tmp/song_info
  id3info "$SONG" > /tmp/song_info
  VALUE=''
  COMPLETE="Y"
  for TAG in "${!id3tags[@]}"
  do
    #VALUE= $(grep $id3tags[$TAG] /tmp/song_info) 
    echo "grepping for ${id3tags[$TAG]}" 
    echo $(grep ${id3tags[$TAG]} /tmp/song_info | head -1 | cut -d: -f2-)  
    echo "end of grep"
    VALUE= $(grep ${id3tags[$TAG]} /tmp/song_info | head -1 | cut -d: -f2-)
    echo "Value of $TAG: $VALUE"
    if [ -z "$VALUE" ]
      then 
        COMPLETE="N"
        echo "$TAG is missing on $SONG"
    else
      echo -n "$TAG=" >> /tmp/song_tags
      echo $VALUE | perl -n -e 's/\W/_/g; s/^_+//; s/_+$//; s/_+/_/g; print "$_\n"' >> /tmp/song_tags
    fi
  done

  if [ "$COMPLETE" == "Y" ]
    then
      echo "##################################################################################"
      echo "# Moving or renaming FILE: $SONG"
      source /tmp/song_tags
 
      mv $SONG /home/clement/Music/${ALBUM}/${TRACK}_${TITLE}.mp3

  fi
done
exit
