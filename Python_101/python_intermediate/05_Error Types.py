### typos - Error Types in Python ###


# SyntaxError

#print "Hola comunidad!" # Error
print("Hola comunidad!")


## NameError ##

#print(language) # no cuenta con una variable definida.

language = "Spanish"
print(language)


## IndexError ##

my_list = ["Python", "Swift", "Kotlin", "Dart", "Javascript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
print(my_list[3])
# print(my_list[7]) # IndexError: list index out of range



## Module not Found Error ##

# import maths # ModuleNotFoundError: No module named 'maths'
import math



## AttributeError ##

import math
# print(math.PI) # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)


## KeyError ## Los indices debes ser 'int' not 'str'

my_dict = {"Nombre" : "Vlad", "Apellido" : "Mano", "Edad" : 34, 1 : "Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # KeyError: 'Apelido'
print(my_dict["Apellido"])


## TypeError ##

# print(my_list["0"]) # TypeError: list indices must be integers or slices, not str
print(my_list[0])
print(my_list[False])


## ImportError ##

#from math import pii # ImportError: cannot import name 'pii' from 'math' (unknown location)
from math import pi
print(pi)


## ValueError ##

my_int = ("10")
#my_int = int("10 Anos") # ValueError: invalid literal for int() with base 10: '10 Anos'
print(int(my_int))
print(type(my_int))


## ZeroDivisionError ##

# print(4/0) ZeroDivisionError: division by zero
print(4/2)

## File not found

# FileNotFoundError: [Errno 2] No such file or directory: '06.1_my_file.txt'