import os

rootFolder = "/media/clement/Maurice/Musique/"

for root, dirs, files in os.walk(rootFolder):
    for name in files:
		if(name == "PROBLEMS.txt"):
			os.remove(os.path.join(root, name))
			print(root)
