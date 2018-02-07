#coding: utf-8
print "PARES E IMPARES"
minimo=input("Escriba un número entero:")
maximo=input("Escriba un número entero mayor o igual que "+str(minimo)+":")
while minimo>maximo:
	print ("¡Le he pedido un número mayor o igual que "+str(minimo)+"!")
	maximo=input("Introduzca otro número mayor o igual que "+str(minimo)+":")
for i in range(minimo,maximo+1):
	if i%2==0:
		print "El número",i,"es par"
	else:
		print "El número",i,"es impar"
