#!/usr/bin/python3
import os
path_components = os.getcwd()
resultaat = path_components.strip(os.sep)
resultaat = path_components.split(os.sep)
while resultaat[0] == '':
    resultaat.remove('')
print (resultaat)
