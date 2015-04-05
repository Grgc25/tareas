def gcd(num1,num2):
	if (num1==num2):
	 respuesta=num1
	elif(num1>num2):
	 respuesta= gcd((num1-num2), num2)  #NOTA: Si quitas "gcd" de las respuestas, cambia bastante el resultado.
	else:
	 respuesta= gcd(num1, (num2-num1))
	return respuesta
	
print("Obtendremos el maximo divisor comun de dos numeros.")	
print("\n")
num1=int(input("Dame el primer numero -> "))
num2=int(input("Dame el segundo numero -> "))
gcd= gcd(num1,num2)
print("el maximo comun divisor de ",num1," y de ",num2," es ",gcd)
