#!/usr/bin/env python

import os
import glob
import json
import pathlib

imageFolder="./w2560-jpeg"

with open("codes.json") as jsonFile:
    countryCodes = json.load(jsonFile)

for file in os.listdir(imageFolder):
    if file.endswith(".jpg"):
        name = pathlib.Path(file).stem
        oldFileName = imageFolder + "/" + file
        try:
            # Clean up new file name
            newFileName = countryCodes[name].replace(" ","-")
            newFileName = newFileName.replace("\\","-")
            newFileName = newFileName.replace("(","")
            newFileName = newFileName.replace(")","")
            newFileName = newFileName.replace(",","")
            newFileName = newFileName.replace("\"","")
            newFileName = newFileName.replace("\'","")
            newFileName = imageFolder + "/" + newFileName + ".jpeg"
            os.rename(oldFileName,newFileName)
        except Exception:
            pass

