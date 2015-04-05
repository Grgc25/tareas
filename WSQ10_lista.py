import statistics #Con esto importamos la libreria de python para calculos de estadistica.

print("Te pedire 10 numeros para calcular varias operaciones")
lista=[] #Esto nos permite crear el espacio para la lista de cosas que necesitamos

for i in range(10): #esta vez queremos 10 numeros. asi que, pondremos un contador 
 i=i+1
 print("Dame un numero, te quedan:",11-i," numeros por introducir")
 num=(float(input("-> ")))
 lista.append(num) #toda esta linea, nos permite agregar un numero mas a la lista de numeros. se podria leer como "agrega el numero "num"al final de la lista "lista""

print("\n")
suma= sum(lista)
promedio=(sum(lista)/10)
desv=statistics.stdev(lista)
print("La suma de los numeros da un total de: ",suma,)
print("La desviacion estandard de los numeros es de: ",desv,)
print("El promedio de los numeros es de: ",promedio,)
