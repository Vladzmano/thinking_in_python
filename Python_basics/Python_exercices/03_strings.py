### Strings ###

my_string = "Mi String"
my_other_string = 'Mi Otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String con \n escapado"
print(my_scape_string)

### Formateo  e inferencias ###

name, surname, age = "Vladimir", "Mano", 34

# %s mostrará el primer texo definido y %d enteros

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %s" %(name, surname ,age))
print("Mi nombre es %s %s y mi edad es %s" %(name, surname ,age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

## como no hcerlo ##

# print("Mi nombre es " + name +  " " + surname + "y  mi edad es " + str(age) )

### desempaquetado de caracteres ###

language = "python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

## Division ##

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

reversed_language = language[0:6:2]
print(reversed_language)

## Reverse ##

reversed_language = language[::-1]
print(reversed_language)

### funciones del sistema o metodos ##

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())

