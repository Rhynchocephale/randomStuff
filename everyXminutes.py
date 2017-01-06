X = 48

def printTime(minute = 0):
	myDict = dict()
	hour = 0
	
	myDict[minute] = [hour]
	while True:
			minute += X
			while minute >= 60:
				hour += 1
				minute -= 60
			if hour < 24:
				if minute in myDict:
					myDict[minute].append(hour)
				else:
					myDict[minute] = [hour]
			else:
				return myDict
	
print(printTime(12))
