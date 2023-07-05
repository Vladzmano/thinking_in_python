### Functions ### Son para resolver problemas concretos que indicaremos, asi evitamos errores y simplificamos el codigo

# def = palavra reservada para crear funcones 

# todo lo que tengfamso tabulado hacia la derecha dentro o despues de crear una funcion va a pertenecer a esta funcion

# la funcion puede generar o recibir codigo par ser procesado

#parametro y argumento so lo mismo

def my_function ():
    print("Esta es una funcion")


my_function ()
my_function ()
my_function ()

def sum_two_values (First_value, Second_value): # sum_two_values funcion para sumar

# es bueno restringir los datos por sus tipos para evitar fallos de ejecucion

    print(First_value + Second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("7", "5")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (First_value, Second_value):
    return First_value + Second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)

## Siempre que se requiera ver el resultado de una funcion debemos crear una variable

def print_name (name ,surname):
    print(f"{name} {surname}")
print_name(surname = "Vlad", name = "Mano") # se le puede dar una vuelta a los parametros, no pueden ser modificado.

def print_name_with_default(name ,surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")
print_name_with_default("Vlad", "Mano")
print_name_with_default("Vlad", "Mano", "Vladzmano")

# numero de parametros dinamico

def print_upper_texts(*texts): # muchas veces se interpresa como tipos de datos diferentes, en ste caso como uma tupla
    for text in texts:
        print(text.upper())

print_upper_texts("Vlad", "Mano")
print_upper_texts("Vlad", "Mano", "Vladzmano")