def invertir(inf):  #invierte
 inf=str(inf)
 inf=inf[::-1]
 inf=int(inf)
 return(inf)
print("Obtendremos los palindromos, no lychrel y candidatos a lychrel de un rango")
print("\n")
numerosenrango=[] #se agregan todos los numeros del rango a esta lista
lychrel=[]

inf=int(input("Cual es el limite inferior? -> "))
sup=int(input("Cual es el limite superior? -> "))
print("el rango de los numeros es de ",inf," a",sup)

for i in range(sup-inf+1): #agrega los numeros a la lista
 numerosenrango.append(inf) #esta es la instruccion que agrega el numero inferior a la lista
 inf=inf+1 #aqui se le suma un numero al numero inferior, para agregar de uno en uno de menor a mayor
#contadores
palindromos=0
nolychrel=0
candidatos=0

for i in numerosenrango:
 volteado=invertir(i)
 if i==volteado: #encuentra los palindromos
  palindromos=palindromos+1
 else: #encuentra los palindromos haciendo iteraciones 30 veces si a la primera no se hace palindromo
  iteracion1=volteado+i
  iteracion2=invertir(iteracion1)
  for i1 in range(30): #aqui se comienza a iterar las 30 veces
   if iteracion1==iteracion2:
    nolychrel=nolychrel+1
    break #break rompe la iteracion cuando se cumple la condicion de la linea anterior
   else:
    iteracion1=iteracion1+iteracion2
    iteracion2=invertir(iteracion1)
    if (i1==29):
     candidatos=candidatos+1
     lychrel.append(i)
print("\n")
print("Hay ",palindromos," numeros que son palindromos")
print("Hay ",nolychrel," numeros que no son lychrel")
print("Hay ",candidatos," numeros que son candidatos a lychrel")
print("\n")
if candidatos!=0: #muestra los que si son lychrel
 print("Los numeros lychrel son:")
 print(lychrel)
