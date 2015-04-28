def check_banana(a):
 archivo=open("bananas.txt",'r')
 cantidad=0
 for i in archivo:
  r=i.lower()#convierte las palabras a minusculas
  sub=r.find('banana')#busca la palabra en el archivo
  while sub !=-1:
   cantidad=cantidad+1
   sub=r.find('banana',(sub+1))
 return(cantidad)
 close("bananas.txt")

cant=check_banana('banana.txt')
print("la palabra banana aparece ",cant," veces en el archivo")
