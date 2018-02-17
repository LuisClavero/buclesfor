#coding: utf-8
cont1=0
cont2=0
cant=input("Cuantos valores va a introducir?")
while (cant<=0):
	cant=input("Error, introduzca otra cantidad de valores superior a 0:")
for i in range(0,cant):
	aux=input("Escriba un número par o impar:")
	if aux%2==0:
		cont1+=1
	else:
		cont2+=1
print "Has introducido",cont1,"pares y",cont2,"impares"


