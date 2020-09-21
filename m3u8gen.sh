#!/bin/bash
# Generator of m3u8 playlists
# By Rey Estrada 
# Github: reyestrada

# Instructions:
# Execute against the main directory
# m3u8gen.sh Music  // where Music is the directory of music
# if not directory provided, script will be executed in current path
# This will read all folders and subfolders (maxdepth = 3) 
# and will generate a playlist per folder
# Playlists will be placed in the current directory
# Playlist names will be the same as playlist folder
# Recommendation: keep names and folders short

if [ -d "$1" ]; then
	echo "Executing script on directory $1"
	cd "$1"
else
	echo "Executing script on directory $PWD"
fi

echo

# find . -maxdepth 1 -type f -printf "%f\n"
# find . -maxdepth 1 -type d -printf "%f\n"

#playlists=$(find . -maxdepth 1 -type d -printf "%f\n" | grep -v Playlists | grep -v ^\.$)
directories=$(find . -maxdepth 3 -type d | sed 's/\.\///g')

while read directory; do 
	playlist=$(find "$directory" -maxdepth 1 -type d -printf "%f" | tr " " "_"
	echo "Generating $playlist...";
	list=$(find "$directory" -maxdepth 1 -type f -iname "*.mp3")
	echo "$list" > "${playlist}.m3u8"
	echo "${playlist}.m3u8 generated!"
	echo
done <<< "$directories"

