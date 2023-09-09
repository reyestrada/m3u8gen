#!/usr/bin/python3
# Generator of m3u8 playlist
# By Rey Estrada 
# Github: reyestrada

# Instructions:
# Execute inside the directory
# m3u8gen_simple.py
# playlist.m3u8 file should be generated

import os

filelist = list(filter(os.path.isfile, os.listdir(os.getcwd())))
playlistName = os.path.basename(os.getcwd()) + ".m3u8"

if playlistName in filelist:
    filelist.remove(playlistName)

playlist = '\n'.join(filelist) + "\n"

f = open(playlistName, "w", encoding='utf-8')
f.write(f"{playlist}")
f.close()
