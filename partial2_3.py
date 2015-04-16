def superpower(a,b):
	respuesta=1
	potencia=1
	while(potencia<b+1):
	 respuesta=respuesta*a
	 potencia=potencia+1
	return respuesta

print("elevaremos el primer numero a la potencia del segundo")
print("\n")
a=int(input("Que numero quieres elevar? -> "))
b=int(input("A que potencia? -> "))
superpower(a,b)
respuesta=superpower(a,b)
print("EL numero ",a," Elevado a la potencia ",b," Da como resultado: ",respuesta,)
