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

# Make array of valid xml string file (Android -> iOs)
def makeArrayOfDictFromXML( lines ):
    arr = []

    for line in lines:
        key = re.search("name=\"(.*?)\"", line, re.M|re.I)
        value = re.search(">(.*?)<\/string>", line, re.M|re.I)
        if key and value:
            arr.append({  key.group(1) : value.group(1) })
    return arr;

# TODO: pass argument for input & out file name
files = readFile('strings.xml')
arr = makeArrayOfDictFromXML(files)

out = open("Localizable.strings", "w+")
for i in arr:
    str = '"{0}" = "{1}" \n\n'.format(i.keys()[0], i.values()[0])
    out.write(str)
out.close