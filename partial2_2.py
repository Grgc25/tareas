def triangulo(p):
	for p in range(0,p+1,1):
		print("T"*p)
	for p in range(p-1,0,-1):
		print("T"*p)
		
p=int(input("Cual quieres que sea el tamano maximo del triangulo? -> "))
triangulo(p)
