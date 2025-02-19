"""
- Listas:
    .insert - Sirve para insertar un elemento en una posición
    .append - Sirve para añadir un elemento al final del arreglo
    .remove - Recorre la lista del arreglo hasta eliminar el elemento indicado
    .pop - Elimina lo que se encuentre en la posición indicada
    .clear - Limpia todo el arreglo
    .extends - Añade los elementos de otra lista
    .sort - Clasifica la lista de elementos
    .sort(nombreLista.reverse) - Clasifica la lista pero al revez
    .index - Se utiliza para encontrar la primera aparición de un valor especificado en una lista
"""

lista = [1,2,3,4,5]
print(lista)
print(lista[0])
print(lista[1:4])
print(lista[:3])
print(lista[2:])
print(lista[0:4:2])
print(lista[-1])
print(lista[-3])
print(lista[::-1])
print(lista[-4:-1])
lista[1:3] = [7,8]
print(lista)
lista.insert(3,9)
print(lista)
lista.insert(-1,9)
print(lista)
lista.insert(9,2)
print(lista)
lista.insert(20,3)
print(lista)
lista.append(6)
print(lista)
lista.remove(9)
print(lista)
lista.pop(1)
print(lista)
lista.pop()
print(lista)
lista.clear()
print(lista)

lista1 = [1,2,3]
lista2 = [4,5,6]
print(lista1)
print(lista2)
lista1.extend(lista2)
print(lista1)

a =  ''
for i in lista1:
    a += str(i)+', '
print(a)

lista3=[2,7,10,1,5]
lista3.sort()
print(lista3)

print(lista3.index(7))