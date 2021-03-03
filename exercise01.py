#!/usr/bin/python3
import os
path_components = os.getcwd()
resultaat = path_components.split("/")
resultaat.remove('')
print resultaat
