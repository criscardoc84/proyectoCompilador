import random
 
def potenciaLista(lista):
    lista_nueva=[]
    for i in range(0,len(lista)):
        lista_nueva.append(lista[i]**i)
    return lista_nueva
 
def imprimirLista(lista,nombre):
    for i in range(0,len(lista)):
        print(nombre + "[" + str(i) + "]=" + str(lista[i]))
 
def leerLista():
    lista=[]
    i=0
    while i < 5:
        lista.append(int(random.randint(0, 10)))
        i=i+1
    return lista
 
A=leerLista()
imprimirLista(A,"A")
print("Potencia:")
B=potenciaLista(A)
imprimirLista(B,"B")