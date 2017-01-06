#if some files in a folder have names where the only difference is capitalisation (test.txt, test.TXT for example), renames them to have really different names

from os import listdir, rename
from os.path import isfile, join, dirname, realpath

scriptFolder = dirname(realpath(__file__))
onlyfiles = [f for f in listdir(scriptFolder) if isfile(join(scriptFolder, f))]
onlyfiles = sorted(onlyfiles, key=lambda s: s.lower())

for i in range(len(onlyfiles)-1):
	if onlyfiles[i].lower() == onlyfiles[i+1].lower():
		rename(onlyfiles[i], ".".join(onlyfiles[i].split(".")[:-1])+"("+str(i)+")."+onlyfiles[i].split(".")[-1].lower())
