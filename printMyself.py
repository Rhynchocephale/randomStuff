import time, random

f = open('printMyself.py')

for line in f:
	for char in line:
		print(char, end="",flush=True)
		if char not in ["\t", " ","\n"]:
			time.sleep(random.randint(5,12)/100)
	
f.close()
