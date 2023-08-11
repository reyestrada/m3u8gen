#!/usr/bin/python3
# Generator of m3u8 playlists
# By Rey Estrada 
# Github: reyestrada

# Instructions:
# Execute against the main directory
# m3u8gen.py Music  // where Music is the directory of music
# if not directory provided, script will be executed in current path
# This will read all folders and subfolders (maxdepth = 1) 
# and will generate a playlist per folder
# Playlists will be placed in the current directory
# Playlist names will be the same as playlist folder
# Recommendation: keep names and folders short

import os, sys, string
# userInput = sys.argv[1] # first argument of command line, same as $1 in shell
# print(userInput)

# userInput = sys.argv # all arguments of command line
# print(userInput)

musicDir = sys.argv[1] if len(sys.argv) >= 2 else './'

#print("Executing script on directory: " + musicDir) if os.path.isdir(musicDir) else sys.exit()

if os.path.isdir(musicDir):
    print("Executing script on directory: " + musicDir)
else:
    print(musicDir + " does not exist")
    sys.exit()

filelist = list(filter(os.path.isfile, os.listdir(musicDir)))

print("filelist is: ")
print(*filelist, sep = '\n')


subMusicDir = list(filter(os.path.isdir, os.listdir(musicDir))) 
print(subMusicDir)

# os.isDirectory(userInput)

# lspwd = os.listdir('./')
# lspwd2 = list(filter(os.path.isfile, os.listdir('./'))) # print only files, not dirs
# lspwd3 = list(filter(os.path.isdir, os.listdir('./'))) # print only dirs, not dirs

# print(lspwd)
# print(lspwd2)
# print(lspwd3)


for root, dirs, files in os.walk(musicDir, topdown=True):
    print(f"root: {root} \ndirs: {dirs} \nfiles: {files}")
    



