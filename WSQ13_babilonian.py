def raiz(n):
 r1=n #la formula del metodo babilonico nos pide intentar adivinar la raiz pero pondremos el mismo numero por poner algo
 c=0
 while(c<10): #entre mas veces se repita el proceso, sera mas acertado. haremos que se repita 10 veces.
   raiz= (r1+(n/r1))/2 #Es la formula del metodo babilonico
   r1=raiz #el numero que suponemos sera cambiado por el resultado de la formula cada vez que se repita la operacion para hacer el resultado mas preciso
   c=c+1 #parte del contador
 return raiz
 
n=float(input("De que numero quieres sacar su raiz cuadrada? -> "))# aqui pedimos el numero
respuesta=raiz(n) #asignamos una variable a la funcion
print("la raiz de ",n," es ",respuesta,)#imprimimos la respuesta
