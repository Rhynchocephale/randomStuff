import random

while True:
	str = ""
	i = random.randint(15,250)
	for j in range(i):
		str += chr(random.randrange(32, 126))
	print(str)
