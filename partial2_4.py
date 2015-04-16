def fibonacci(espacio):
 if (espacio==0) or (espacio==1):
  return espacio
 elif (espacio<0):
  return ("no se valen los numeros negativos")
 else:
  respuesta=fibonacci(espacio-1)+fibonacci(espacio-2)
  return respuesta
espacio=int(input("Que espacio de la serie de fibonacci quieres saber? -> "))
fibonacci(espacio)
respuesta=fibonacci(espacio)
print("\n")
print("La respuesta es: ",respuesta,)
