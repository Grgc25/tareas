def dist(x1,x2,y1,y2):
	respuesta=(((x2-x1)**2)+((y2-y1)**2))**.5
	return respuesta
print("sacaremos la distancia entre dos puntos")
print("\n")
print("ubica el primer punto")
A=[]
B=[]
x1=int(input("distancia del primer punto en x -> "))
A.append(x1)
y1=int(input("distancia del primer punto en y -> "))
A.append(y1)
print("\n")
print("ubica el segundo punto")
x2=int(input("distancia del segundo punto en x -> "))
B.append(x2)
y2=int(input("distancia del segundo punto en y -> "))
B.append(y2)
print("\n")
print("el primer punto sera ubicado en: ",A,)
print("el segundo punto sera ubicado en: ",B,)
dist(x1,x2,y1,y2)
respuesta=dist(x1,x2,y1,y2)
print("\n")
print("la distancia entre los dos puntos es de ",respuesta,)


