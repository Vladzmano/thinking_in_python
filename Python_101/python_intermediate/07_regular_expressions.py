### Regular  expressions - expresiones regulares ###


## match ## encontrar elementos en una cadena de texto.

import re

my_string = "Esta es la leccion numero 7: Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6 : Manejo de ficheros"

match = (re.match("Esta es la leccion", my_string, re.I))
print(match)
start, end = match.span()
print(my_string[start:end])

# comprobar si conteamos o no con los elementos que buscamos en una cadena de texto

match = (re.match("Esta es la leccion", my_other_string))
# if not (match == None):
# if match =/= None: tambien funciona.
if match is not None:
    print(match)
    start, end = match.span()
    print(my_string[start:end])

print(re.match("Expresiones regulares", my_string))


## search ## encuentra la primera ocurrencia del todo 


search = (re.search("Leccion", my_string, re.I))
print(search)
start, end = search.span() # imprime el elemento especifico
print(my_string[start:end])


## findall ## muestra cuentas veces aparece en nueesta cadena de texto


findall = (re.findall("Leccion", my_string, re.I)) # I se utiliza para ignorar el formato del texto, ya sea minuscula o mayuscula.
print(findall)

## split ## busca un patrol en 2 puntos y divide a partir de alli

print(re.split(":",my_string))


## sub ## se utiliza para substituir elementos. se a me ayuscula a minuscula etc


print(re.sub("[l|L]]eccion", "LECCION", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))