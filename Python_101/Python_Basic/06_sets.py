### Sets ### de base tiene un array o vector- su forma de guardar los elementos es desordenada. no tenems idea de donde estan los elementos.
#
my_set = set()

print(type(my_set))
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # inicialmente es un diccionario

my_other_set = {"34", "1.70", "Vlad", "Mano"}
print(type(my_other_set))

print(len(my_other_set))


my_other_set.add("vlox")
print(my_other_set) # un set no es un aestructura ordenada y no admite elementos repetidos


print(my_other_set)

print("Vlad" in my_other_set)
print("Falde" in my_other_set) # se pueden buscar elementos y general un bool

my_other_set.remove("Vlad")
print(my_other_set)

my_other_set.clear() # vacia toso los elementos pero no elimina el objeto o set en este caso
print(len(my_other_set))

#del my_other_set esto es un error


my_set = {"1.70", "Vlad", "Mano"}
my_list = list(my_set)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"javascript, C#"})) # con esta opcion no se duplican los elementos, solo agrega elementos nuevos.
#lo antes mostrado solo se muestra como resultados en el print y no se almacena en la variable.

print(my_new_set.difference((my_set)))


