### Lambdas ###

# se entiende como una funcion, pero son unciones anonimas, no tiene nombre
# puede tener parametros de entrada
# un lambda se puede almacenar en una variable. Funcion == Metodo
# funciones muy concretas.
# para funcines que no sean de proposito general

sum_two_values = lambda number1, number2: number1 + number2
print(sum_two_values(29, 3))


multiplu_values = lambda first_value, second_value: first_value * second_value - 3
print(multiplu_values(2,4)) 

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))