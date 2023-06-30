### Listas / lists =/= arrays / arreglos

my_list =  list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 18 , 60, 17, 30, 30]


my_other_list = [35, 1.77, "vlad", "Mano"]

print(my_list)
print(len(my_list))

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list.count("vlad"))  # cuenta el valor o la cantidad de elementos del mismo tipo dentro de un alista 
print(my_list.count(30)) # cuenta el valor o la cantidad de elementos del mismo tipo dentro de un alista
#print(my_other_list[4]) Indexerror
#print(my_other_list[-5]) Indexerror

age, height, name, surname = my_other_list # si retiramos un elemento da error, ya que el desempaquetado se hace de toda la lista.
print(name)

'''
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print() # es una forma de rebiscarse y esto no se recomienda

'''

print(my_list + my_other_list)
#print(my_list - my_other_list) esto es un error

## Dynamic type ##

my_other_list.append("VladDev") # inserta un elemento al final de la lista
print(my_other_list)

my_other_list.insert(1, "Rojo") # inserta un elemento en la lista
print(my_other_list)

my_other_list[1] = "Negro" # en esta parte cambiamos un elemento antes definido
print(my_other_list)

#my_other_list.remove("Negro")
#print(my_other_list)

my_list.remove(30) # alimina un objeto en concreto conocido en la lista
print(my_list)


## Cues / colas ##


print(my_list.pop()) # pop elimina el elemento y mustra cuel fué, muesra el indice.
print(my_list)

print(my_list.pop(2))
print(my_list)

del my_list[2] # del elimina por indice del elemento de la lista.
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)


print(my_new_list[1:3])

print(my_new_list[0])


##################################
my_list = "Hola Python"
print(my_list)
print(type(my_list))
