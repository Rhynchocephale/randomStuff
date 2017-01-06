for a in range(10):
	for b in range(10):
		for c in range(10):
			for d in range(10):
				for e in range(10):
					if (10*d+a-c == 10*a+e) and (10*b+c+e==10*c+a) and (10*e+d-b==10*d+b):
						print('a: '+str(a))
						print('b: '+str(b))
						print('c: '+str(c))
						print('d: '+str(d))
						print('e: '+str(e))
						print('10a+d+10e+a: '+str(11*a+d+10*e))
						print('------')
