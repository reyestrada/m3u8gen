#!/bin/bash
# Generator of m3u8 playlists
# By Rey Estrada 
# Github: reyestrada

# Instructions:
# Execute against the main directory
# m3u8gen.sh Music  // where Music is the directory of music
# if not directory provided, script will be executed in current path
# This will read all folders 
# and will generate a playlist per folder
# Playlists will be placed in Playlists folder
# Playlist names will be the same as playlist folder
# Recommendation: keep names and folders short

if [ -d "$1" ]; then
	echo "Executing script on directory $1"
	cd "$1"
else
	echo "Executing script on directory $PWD"
fi

echo

if [ -d Playlists ]
then 
	echo "Playlists directory exist"
	echo
else
	echo "Playlists directory does not exist, creating it..."
	mkdir Playlists
	echo
fi

# find . -maxdepth 1 -type f -printf "%f\n"
# find . -maxdepth 1 -type d -printf "%f\n"

playlists=$(find . -maxdepth 1 -type d -printf "%f\n" | grep -v Playlists | grep -v ^\.$)

while read playlist; do 
	echo "Generating $playlist...";
	list=$(find "$playlist" -maxdepth 1 -type f -iname "*.mp3" -printf "../${playlist}/%f\n")
	echo "$list" > "Playlists/${playlist}.m3u8"
	echo "Playlists/$playlist.m3u8 generated!"
	echo
done <<< "$playlists"

