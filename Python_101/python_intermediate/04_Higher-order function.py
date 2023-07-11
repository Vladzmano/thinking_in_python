### Higher-order function / Funciones de orden superios ###

# como somos capaces de definir funciones dentro de funciones y operar con ellas
# existes Higher-order function del sistema.
# funciones que son capaces de ejecutar mas funciones
#Que tengamos la posibilidad que nuetsras funciones realizaen varias operaciones

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_values, second_values, f_sum):
    return f_sum(first_values + second_values)

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))


## Closures ## Funciones que retornan otras funciones. Paradigmas asincronos - listeners

def sum_ten(origial_value):
    def add(value):
        return value + 10 + origial_value
    return add

add_closures = sum_ten(1)
print(add_closures(5))
print((sum_ten(5))(1))




## Build-in Higher-order function ## 


## Map ## - con un listado iterable genera otro listado iterabe con funcion a la funcion que le hemos pasado

numbers = [2, 5, 10, 21, 3, 30]

def multiply_two(number):
    return number *2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

## filter ##

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))  #A opcion 1
print(list(filter(lambda number: number > 10, numbers))) #B opcion 2



## reduce ##

# opera con un valor mas lo acumulado.

# necesita una funcion que cumpla el criterio, opera entre los valores que recorre.

"""[2, 5, 10, 21, 3, 30]"""

def sum_two_values(first_values, second_values,):
    print(first_values)
    print(second_values)
    return first_values + second_values

print(reduce(sum_two_values, numbers))
