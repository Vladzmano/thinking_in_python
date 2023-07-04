### Conditionals ### representa la manera de estabelcer el flijo de ejecucion del nuestro codigo

# si no colocamos un valor concreto en la variable los condicionales tomaran una descicion booleana

my_condition = False

if my_condition: # es lo mismo que if my_condition == True
    print("Se ejecuta la condicion de if")\
    
my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condicion de segundo if")


if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")


print("La ejecucion continua")

my_string = ""

if not my_string: # este if verifica si no vacio es True
    print("Mi cadena de texto es vacia")
if my_string == "Mi cadena de textoooo":
    print("Mis cadenas de texto coinciden") 