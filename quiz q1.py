x=int(input("Dame un valor -> "))
def triangle(x):
 for x in range (0,x+1):
  print("T"*x)
 for x in range (x+1,-1,-1):
  print("T"*x)

triangle(x)
