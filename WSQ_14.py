def calculate_e(precision):
 x=precision
 e=(1+1/x)**x
 return (e)
precision=int(input("Cuantos decimales necesitas? -> "))
respuesta= calculate_e
print("el numero e, con los decimales",precision," es: ",respuesta)
