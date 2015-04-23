def dot_product(L1,L2):
 if (len(L1) != len(L2)):
  return "NOPE!"
 else:
  total=0
  for (x,y) in zip(L1,L2):
   total= total + x*y
  return total

print("Obtendremos el producto punto de la multiplicacion de dos listas")
print("\n")
print("Comenzaremos por crear la primera lista. Recuerda que ambas listas deben tener la misma cantidad de numeros.")
L1=[]
answer="si"
while (answer=="si"):
 n=int(input("Introduce un numero ->"))
 L1.append(n)
 print(" La primer lista tiene ",len(L1)," Numeros")
 print(L1)
 print("\n")
 answer= input("Quieres agregar otro numero? (si/no) -> ")

 
print("\n")
print("Ahora toca la segunda lista")
L2=[]

while ((len(L1))>len(L2)):
 n=int(input("Introduce un numero ->"))
 L2.append(n)
 print(" La segunda lista tiene ",len(L2)," Numeros")
 print(L2)
 print("\n")
 print("Te quedan ",(len(L1)-len(L2))," Numeros por agregar.")
 print("\n")
print("La primer lista es: ",L1)
print("La segunda lista es: ",L2)
print ("El resultado del producto punto entre ambas listas es: ",(dot_product(L1,L2)))
#Hecho por Guillermo Gomez
