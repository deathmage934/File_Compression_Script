import sys
import os
import zip
import unzip

if not os.path.exists(sys.argv[1]):
    print("INVALID FILE PATH")
elif len(sys.argv) > 2 and sys.argv[2] == '--u': #command for unzipping the file
    unzip.unzip(sys.argv[1])
elif len(sys.argv) > 2 and sys.argv[2] == '--z': #command for zipping the file
    if not os.path.exists(sys.argv[1][:-4]):
        os.makedirs(sys.argv[1][:-4])
    zip.zip(sys.argv[1])
else: # no tags will zip the file and then unzip. this is for testing purposes
    if not os.path.exists(sys.argv[1][:-4]):
        os.makedirs(sys.argv[1][:-4])
    zip.zip(sys.argv[1])
    unzip.unzip(sys.argv[1][:-4])