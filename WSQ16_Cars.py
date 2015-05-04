arcvhivo=open("93cars.dat.txt","r")
mpg_C=0
mpg_A=0
pp_V=0
cars=0
f=1
for line in archivo:
    if f%2==1:
        mpg_C=mpg_C+float(line[52:54])
        mpg_A=mpg_A+float(line[55:57])
        pp_V=pp_V+float(line[42:46])
        cars=cars+1
    f=f+1
mpgc=round(mpg_C/cars,6)
mpga=round(mpgh/cars,6)
ppv=round(mp/cars,6)

print("City MPG: ", mpgc)
print("Highway MPG: ",mpga)
print("Average midrange price of the vehicles: ",ppv)
