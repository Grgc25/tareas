def find_threes(lista): #funcion para crear la nueva lista con elementos divisibles entre 3
 n_lista=[]
 for num in lista:
  if (num%3 ==0 ):
   n_lista.append(num)
 return n_lista

lista=[] #nueva lista
ans="si"

print("Crearemos una lista.")
print("\n")

while ans=="si": #Elementos de la lista
 num=int(input(" Introduce un valor -> "))
 lista.append(num)
 cant=len(lista)
 print("tienes ",cant," Valores en la lista")
 ans=input(str("Quieres agregar otro numero? (si/no) -> "))
 print("\n")

 #llamado de funciones
find_threes(lista)
lista_divisible=(find_threes(lista))
suma_divisibles=sum(find_threes(lista))

#salidas
print("\n")
print("La lista, ",lista, "tiene ",cant," valores.")
print(lista_divisible," son divisibles entre 3")
print("el resultado de la suma de estos numeros es de ",suma_divisibles)
