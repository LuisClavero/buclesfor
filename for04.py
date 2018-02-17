#coding: utf-8
cont=0
cant=input("Cuantos valores va a introducir?")
while (cant<=0):
	cant=input("Error, introduzca otra cantidad de valores superior a 0:")
cant1=float(input("Introduzca un numero:"))
for i in range(0,cant+1):
	cant2=float(input("Introduzca un numero mayor que "+str(cant1)+":"))
	if (cant1>cant2):
		print "¡"+str(cant2)+" no es mayor que "+str(cant1)+"!"
	cant1=cant2
