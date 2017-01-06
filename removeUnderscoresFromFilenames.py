folder = "/home/clement/Music/VGL 2016/LET ME TELL YOU A STORY"
import os
for root, dirs, filenames in os.walk(folder):
	for filename in filenames:
		fullpath = os.path.join(root, filename)
		os.rename(fullpath, fullpath.replace("Random Encounter - LET ME TELL YOU A STORY - ",""))
