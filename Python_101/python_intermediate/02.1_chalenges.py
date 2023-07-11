### Resolver desafios usando lo aprendido en python ###

"""
for i in range(1, 101): ## Rango se utiliza para imprimir numeros
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
"""

def fizz_b():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)
fizz_b()


"""
Es un Anagrama? (y Palindromos)
Escribe una funcion que reciba dos palabras (string) y retorne
verdadero o falso (bool) segun sean o no anagramas
- Un anagrama consite en foramar una palabra retornando TODAS
  las letas de otra palabra inicial
- NO hace falta comprobar que ambas palabras existen.
- Dos palabras exactamene iguales no so anagramas
"""
 
# lower es una operacion para cadenas de texto o aray de caracteres
# se pasa a minuscula con ese string se puede ordenar y comprar.
# 'sorted' va a ordernar todas las letras de las palabras

def is_anagrama(word_one, word_two):
    if word_one == word_two:
       return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagrama("Amor", "Roma"))


"""
LA SUCESION O SERIE DE FIBONACCI

Escribe un programa que imprima los 50 primeros numeros de la scesion de Fibonacci empezando en 0.
- La serie de Fibonacci se compone por una sucesion de numerios en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13 ...

"""

# se puede ejecutar o definir un rango y poder lanzar un for a partir de el . se puede ejecutar un bucle sobre un rango.
# se puede solventar con recurrencia.
# iterar == Recorrer una lista o indice.

def fibonacci():

    prev = 0
    next = 1

# Se requiere de indice para iterar con el rango en este caso

    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib

fibonacci()


"""
Es un numeor primo?

Escribe un programa que se encargue de comprobar si un numeor es primo o no.
Hecho esto, imprime los numeros primos entre 1 y 100

"""
# numero natural mayor que uno que tiene unicamente 2 divisores positivos distintos de el mismo y 1

def is_prime():

   for number in range(1, 101): 
        
    if number >= 2:
        
        is_divisible = False
    
        for index in range(2, number):
            if number % index == 0:
               is_divisible = True
               break

        if not is_divisible:        
            print(number)

is_prime()

"""
Invertir cadenas de texto

Crea un program que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automatica
- Si le pasamos "Hola mundo" nos retornaria "odnum aloH"
"""
# 'str' cadena de texto 

def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0,len(text)):
        reversed_text += text[text_len - index -  1]
    return reversed_text

print(reverse("Hola mundo"))
