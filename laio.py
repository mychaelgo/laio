#!/usr/bin/python

# Laio (Localize Android iOS)
# Created by @mychaelgo

import re

# Read file
def readFile( fileName ):
    f = open(fileName, "r")
    lines = f.readlines()
    f.close
    return lines;


files = readFile('strings.xml')

s = files[1]
key = re.search("name=\"(.*?)\"", s, re.M|re.I)
value = re.search(">(.*?)<\/string>", s, re.M|re.I)

print key.group(1)
print value.group(1)