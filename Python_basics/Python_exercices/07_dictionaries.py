### dictionaries ### este recurso facilita el acceso y la consulta de datos mediante clave valor

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))


my_other_dict = {"Nombre" : "Vlad", "Apellido" : "Mano", "Edad" : 34, 1: "Python"}

my_dict = { #datos de clave-valor xxxx:000,
    "nombre" : "Vlad",
    "Apellido" : "Mano", 
    "Edad" : 34, 
    "lenguajes": {"Python", "swift", "Kotlin"},
    1:1.77
      }


print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

#print(my_dict["Nombre"])

my_dict["Nombre"] = "pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["calle"] = "Calle Flademir"
print(my_dict)

del my_dict["calle"] # esto es para eliminar elementos individuales en dict
print(my_dict)

print("Apellido" in my_dict)
print("Edad" in my_dict) # comprobamos que existe en el diccionario

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

#y_new_dict = my_other_dict.fromkeys(("Nombre", 1))
#print(my_new_dict) #esta es una forma de crear un nuevo diccionario vacio

my_list_dict = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list_dict))
print(my_new_dict)

my_list_dict = dict.fromkeys((my_list_dict))
print(my_list_dict)


my_list_dict = dict.fromkeys((my_dict)) #creando un diccionario nuevo copiando las keys, copiando las claves de un dict existente
print(my_list_dict)


my_list_dict = dict.fromkeys(my_dict,("Vlad","Mano"))
print(my_list_dict)

