### Class - Clases ### podremos dotar de principio y fin a un objeto. Tambien se puede interpretar como dar contexto a las funciones de nuestro codigo.

# Los nombres de las clases las escribimos con 'camel case'
# las clases se deben llamar desde fuera, no mesclar funcion con clase
# LAS VARIABLES DE CLACES PUEDEN SER PRIVADAS DE LECTURA

class MyEmptyPerson: #class palavra clave reservada del sistema.
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):         # constructor de clase, donde se establecen valores de una veriable/clase 'self se refiere a la instancia en si misma'
        self.full_name =   f"{name} {surname} ({alias})"   ## propiedad publica  -- # El self es obligatorio pra crear esta regla o limitacion
        self.__name = name                                          ## propiedad privada
        
    def ger_name (self):
        return self.__name                                             #  Podemos crear propiedades definidad dentro o fuera de la clase

    def walk(self): 
        print(f"{self.full_name} Esta caminando")                     # contsructor , parte de la clase que realiza la accion

my_person = Person("Vlad", "Mano")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Vlad", "Mano", "Manodev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Luiz de Leon (el loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)


# este objeto no s sirve para definir una entidad
# En python se puede cambiar el tipo de dato que es esta definiendo.