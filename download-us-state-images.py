#!/usr/bin/env python

import os
import glob
import json
import pathlib
import requests

#response = requests.get("https://flagpedia.net/us-states")
#print(response.text)
#al.png
baseImageURL="https://flagcdn.com/w2560/us-"

imageFolder="./w2560-us-states/"

with open("us-state-codes-data.json") as jsonFile:
    stateCodes = json.load(jsonFile)

for state in stateCodes:
#    print(state['State'],state['Code'])
    stateName = state['State']
    stateCode = state['Code'].lower()
    imageURL = baseImageURL + stateCode + ".png"
    imageFileName = imageFolder + stateName + ".png"
    print("Downloading:",imageURL)
    img_data = requests.get(imageURL).content
    with open(imageFileName, 'wb') as handler:
        handler.write(img_data)


