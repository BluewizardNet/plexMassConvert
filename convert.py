#!/usr/bin/python3
#!/opt/homebrew/bin/python3


###############################################################################
# Convert mass amount of files from within plex from ts to mkv
#
###############################################################################


import sys
import os
from pathlib import Path
import shutil
import re

fileExtension=".ts"
newFileExtension=".mkv"
tmpFileDir="/tmp/plexMassConvert"
comcutLocation="/usr/local/bin/comcut"
handBrakeCli="/usr/bin/HandBrakeCLI"
#handBrakeCli="~/bin/HandBrakeCLI"
handBrakeOptions="-e x264 -f av_mkv -E av_aac -R auto -6 stero -B 160 --audio-fallback ac3 --encoder-preset faster -q 23 -2 --encoder-level=\"3.1\" --vfr --decomb bob -i "

def findItems(imagePath, rootDirectory, destinationRootDirectory):
    print("Images Path: ", imagePath)
    files = os.scandir(imagePath)
    for entry in files:
        if not entry.name.startswith("."):
             if os.path.isfile(os.path.join(imagePath, entry)):
                 if entry.name.endswith(fileExtension):
                    print("Entry: ", entry.name)
                    subDirectorySplit = imagePath.split(rootDirectory)
                    # subDirectory has the leading /
                    subDirectory = subDirectorySplit[1]
                    print("\n\n\n***SubDirectory: " + subDirectory)

                    sourcePath = rootDirectory + subDirectory + "/" + entry.name
                    fullPathDIR = tmpFileDir + subDirectory 
                    fullPathTMP = tmpFileDir + subDirectory + "/" + entry.name
                   
                    Path(fullPathDIR).mkdir (0o755, True, True)
                     
                    shutil.copyfile(sourcePath, fullPathTMP)
                    print("Running ComCut on File: ", fullPathTMP)
                    commandComskip = comcutLocation + " \"" + fullPathTMP + "\""
                    os.system(commandComskip)
                    print("Finished comcut")
                    print("Starting Encoding")

                    destinationFileName = entry.name.replace(fileExtension, newFileExtension)
                    destinationFullPath = destinationRootDirectory + subDirectory + "/" + destinationFileName
                    tmpDestinationFullPath = fullPathDIR + "/" + destinationFileName

                    commandHandbrakeCLI = handBrakeCli + " " + handBrakeOptions + "\"" + fullPathTMP + "\" -o \"" +  tmpDestinationFullPath + "\""
                    commandHandbrakeCLI = re.sub(r'([\`])', r'\\\1', commandHandbrakeCLI)
                    print("HandbrakeCLI: ", commandHandbrakeCLI)
                   
                    os.system(commandHandbrakeCLI)
                    print("Finished Encoding")

                    print("tmpDestinationFullPath: " + tmpDestinationFullPath)
                    print("dstinationFullPath: " + destinationFullPath)
                    shutil.move(tmpDestinationFullPath, destinationFullPath)
                    Path(fullPathTMP).unlink()
                   
             else:
                 if entry.is_dir:
                    print("DIR: ", entry.name)
                    subDirectorySplit = imagePath.split(rootDirectory)
                    #subDirectory has the leading /
                    subDirectory = subDirectorySplit[1]

                    fullPath = destinationRootDirectory + subDirectory + "/" + entry.name
                    Path(fullPath).mkdir (0o755, True, True)
                    findItems(os.path.join(imagePath, entry), rootDirectory, destinationRootDirectory)



if __name__ == "__main__":
    print(sys.argv)
    print("arg1:", sys.argv[1])
    print("arg2:", sys.argv[2])
    findItems(sys.argv[1], sys.argv[1], sys.argv[2])



