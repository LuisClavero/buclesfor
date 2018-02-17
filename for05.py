#coding: utf-8
cont=0
cant=input("Cuantos valores va a introducir?")
while (cant<=0):
	cant=input("Error, introduzca otra cantidad de valores superior a 0:")
for i in range(0,cant):
	aux=input("Escriba un número:")
	if aux<0:
		cont+=1
print "Ha introducido",cont,"numeros negativos"
