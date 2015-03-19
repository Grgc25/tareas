def factor(num): #Primero, definimos la funcion
 suma=1 #recuerda que si multiplicas por cero es cero por eso la variable suma es 1, 1 es el limite, NADA QUE VER CON EL CONTADOR
 while num>=1: #con esto va bajando el numero que introdujiste hasta que sea mayor o igual que uno porque no se puede multiplicar por cero
  suma=suma*num #aqui cambia el valor "1" que teniamos en la suma porque se multiplica por el numero que insertaste
  num=num-1 #nos asegura que el contador esta bajando hasta que llegue al uno y satisfacer la condicion de la linea 3
 print(suma)
 
print("Hola, obtendremps el factorial de un numero.")
print("\n")

respuesta="si"
while respuesta=="si": 
 print("Escribe el numero entero:")
 num=int(input("-> "))
 if num<0:
  print("Numero invalido")
 elif num==0:
  print("el factorial de 0 es 1")
 elif num==1:
  print ("El factorial de 1 es 1")
 else:
  factor(num)
 respuesta=input("Quieres calcular otro valor? si/no: ")
