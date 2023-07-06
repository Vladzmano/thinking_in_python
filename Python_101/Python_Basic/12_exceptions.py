### Exceptions Handling ### control de errores

# debemos tener mecanismos activos para evitar errores.

"""
Try:
    {Run this code}
exept
    {Execute this code when there is an exception}
else:
    {No exceptions? Run this code}
finally:
    {Always run this code}
"""

numberOne = 5
numberTwo = 1
numberTwo = "1"

# tenesmo un criterio de aceptacion de loa valores ingresado inicialmente, esto no ayuda con el control de errores eficiente
"""
if type(numberTwo) == int:
    print(numberOne + numberTwo) 
else:
    print("No se cumple")
"""

# try and except son palavras reservadas del sistema.

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

    ## try - except - else

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except: # no se puede omitir el except
    print("Se ha producido un error")
else:
    # se ejecuta si no se presenta un excepcion
    print("La ejecucion continua correctamente")
finally:
    # se ejecuta siempre
    print("la ejecucion continua")

## Captura de excepciones por tipo ##

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError: # no se puede omitir el except
    print("Se ha producido un ValueError")
except TypeError: # no se puede omitir el except
    print("Se ha producido un TypeError")


# captura de la informacion de la excepcion -- 
# Tiene sentido dar feedback al usuario del programa para que sepa de que se trata el error
# se puede crear un Log error para almacenar los errores

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error: # al macena el error y mustra las especificacioines del mismo
    print(error)
except Exception as exceptions:
    print(exceptions)