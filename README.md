# plexMassConvert
Take Plex files and do a mass comskip and convert them from ts to mkv

# Pre-Requirements
Must ensure the convert.py script first line is where your python3 exists at

## Dependencies

### comskip

This is part of the following github repo:

[https://github.com/erikkaashoek/Comskip]

### comcut 

This is part of the following github repo:

[https://github.com/BrettSheleski/comchap]

### comskip.ini

comskip.ini needs to be copied to the user running the command home directory.



## macOS
TBD

## Linux

Run in the background with nohup.

Must run from the directory that contains the script.
comskip.ini needs to be copied to the users home directory as .comskip.ini

nohup ./convert.py /mnt/recordings/McHale\'s\ Navy\ \(1962\) /mnt/storage/tvConversion/McHale\'s\ Navy\ \(1962\) 2>&1 &


## Known Errors

If a ts file is not large enough the comskip may not run correctly and generate an EDL file.
If this is the case the whole script dies.

Remove the problematic ts file and start over


