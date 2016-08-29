def compounded_principal(time):
	 p = 10000
	 r = 0.08
	 n = 1
	 A = p* (1+(r/n)) ** (n * time)
	 return int(A)