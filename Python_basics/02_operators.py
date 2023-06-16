### Aritmetic Operators ###

print(3 + 4) # Adition
print(3 - 4) # Substraction
print(3 * 4) # Multiplication
print(10 % 4) # Module or division
print(10 // 3) # floor división para calcular el resultado mas proximo
print(2 ** 3) # exponentes / exponenciales

print(2 ** 3 + 3 - 7 / 1 // 4)

# concatenar cadenas de texto

"""
str = transfor into string
int = transforn into integer
"""

print("Hola " + "Python " + "Que tal?")

print("Hola " + str(5)) # para concatenar enteros y string
print("Hola" * 5)
print("Hola" * (2 ** 3)) 

my_int = 2.5 * 5
print("Hola" * int(my_int))

### Comparative Operators ###

print(3 > 4) # greater than
print(3 < 4) # less than
print(3 >= 4) # Greater or equal to
print(3 <= 4) # Less or equal to
print(3 == 4) # Equal to
print(3 != 4) # Diffrent from

### Logic Operators ###

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" > "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or "Hola" > "Python" and 4 == 4)
print(not(3 > 4 ))
