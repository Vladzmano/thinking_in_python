### Tuplas / tuples ### las tuplas y listas son diferentes porque no es posible cambiar valores, son inmutables a diferencia de las listas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "vlad", "mano", "zam")

print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("vlad"))
print(my_tuple.index("mano"))
print(my_tuple.index("vlad"))

#my_tuple[1] = 1.80
#print(my_tuple) Esta operacion no es valida en tuplas ya que no es posible modificar datos.
#no cuenta ocn operacion insert

my_sum_tuple = my_tuple + my_other_tuple
print(my_other_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "VLZM"
my_tuple.insert(1, "Azul")
print(tuple(my_tuple))

#del my_tuple[2] esto es un error.

#del my_tuple
#print(my_tuple) Esto wa un error no es un borra, esto elimina nuestra variables.
