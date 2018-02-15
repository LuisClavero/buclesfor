#coding: utf-8
num=input("Escriba un número:")
div=2
while num<0:
	num=input("Le he pedido un numero mayor que cero, escriba otro:")
for i in range(0,num):
	if num%div==0:
		print div,"es divisor de",num
		div=div+1
	else:
		div=div+1	
print "Fin"


