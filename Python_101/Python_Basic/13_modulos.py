### Modules ### los modulos o ficheros no deben iniciar con numero para ser utilizados en nustro programa

#import my_module

from my_module import sumValue, printValue

#my_module.sum(5, 51, 2)
#my_module.printValue("Hola Python!")

sumValue(5, 3, 1)
printValue("Hola Python!")


## modulos del sistema (modulos build-in) ##


import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_VALUE

print(PI_VALUE)

 
