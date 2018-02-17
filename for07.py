#coding: utf-8
ent1=input("Escriba un número entero:")
ent2=input("Escriba un número entero mayor que "+str(ent1)+":")
suma=0
while (ent2<ent1):
	print "Le he pedido un numero mayor que",ent2
	ent2=input("Escriba un número entero mayor que "+str(ent1)+":")
for i in range(ent1,ent2+1):
	suma+=i
print "La suma desde "+str(ent1)+" hasta "+str(ent2)+" es:",suma
