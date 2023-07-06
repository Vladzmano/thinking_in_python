### comprecion de listas - list comprehension ###


my_original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8] #gange
print(my_original_list)


my_list = [i for i in range(8)] # esto es un bucle para iterar
print(my_list)

my_range = range(8)
print(list(my_range))

my_list = [i * i for i in range(8)] # "i" corresponde a cada uno de los elementos d ela lista
print(my_list)


def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)] # "i" corresponde a cada uno de los elementos d ela lista
print(my_list)