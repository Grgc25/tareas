import statistics

def readNumbersFromFile(n):
 f=open("random_numbers.txt","r")
 suma=0
 cant=0
 lista=[]
 for i in f:
  suma=suma+float(i)
  cant=cant+1
  lista.append(float(i))
  stdrd=statistics.stdev(lista)
 close("random_numbers.txt")
 print('la suma de los valores es: ',suma)
 print('la cantidad de valores es: ,',cant)
 print('El promedio es: ',(suma/cant))
 print('la desviacion estandard es: ',stdrd)

readNumbersFromFile("random_numbers.txt")
