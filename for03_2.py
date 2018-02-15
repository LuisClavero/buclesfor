#coding: utf-8
cont=0
cant=int(input("Cuantos valores va a introducir?"))
while (cant<=0):
	cant=int(input("Error, introduzca otra cantidad de valores superior a 0:"))
aux=float(input("Introduzca un numero:"))
for i in range(0,cant):
	aux2=float(input("Introduzca un numero mayor que "+str(aux)+":"))
	if aux<aux2:
		print "Imposible"
		aux=float(input("Error, introduzca un numero mayor:"))
