#!/usr/bin/python3
# Generator of m3u8 playlists
# By Rey Estrada 
# Github: reyestrada

# Instructions:
# Execute inside the directory
# m3u8gen_simple.py
# playlist.m3u8 file should be generated

import os
# import sys, string, re

filelist = list(filter(os.path.isfile, os.listdir(os.getcwd())))
filelist.remove("playlist.m3u8")
playlist = '\n'.join(filelist) + "\n"

f = open("playlist.m3u8", "w", encoding='utf-8')
f.write(f"{playlist}")
f.close()
