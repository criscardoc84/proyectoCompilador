# Retornar la suma de los elementos de una lista.
import random

def sumarLista(lista):
    sum=0
    for i in range(0,len(lista)):
        sum=sum+lista[i]
    return sum
 
def imprimirLista(lista,nombre):
    for i in range(0,len(lista)):
        print (nombre + "[" + str(i) + "]=" + str(lista[i]))
 
def leerLista():
    lista=[]
    i=0
    while i < 5:
        lista.append(int(random.randint(0, 5)))
        i=i+1
    return lista

A=leerLista()
imprimirLista(A,"A")
print ("Suma = " + str(sumarLista(A)))