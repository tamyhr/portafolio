mi_lista=[1,2,3,4,5]
print(mi_lista)
lista_vacia=[]
lista_combinada=[1,"hola",3.14,True]

lista_vacia.append( "python")
print(lista_vacia)
mi_lista.append(6)
print(mi_lista) 

mi_lista.insert(2,10)
print(mi_lista)

print(mi_lista[5])
print(mi_lista[-2])

sub_lista=lista_combinada[2:5]

cadena="Bienvenidos a curso de ciencia de datos"
lista_cadena=cadena.split()
print(lista_cadena)

palabras=["pyhton","es","un","lenguaje","interpretado"]
frase=" ".join(palabras)
#print(frase)

matriz=[(1,2),(3,4),[True,"a"]]

print(matriz)
print(matriz[2][0])       

nueva_lista=[expresion for item in iterable if condicion]
              
dobles=[]
for in numero mi lista:
    dobles.append(numero*2)
print(dobles)

dobles2=[numero*2 for numero in mi_lista if numero<10]
print(dobles2)