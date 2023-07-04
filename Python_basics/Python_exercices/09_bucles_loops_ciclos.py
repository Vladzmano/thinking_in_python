### Loops - cycles ### iterar es repetir algo, pasar por el codigo varias veces

## While ##

my_condition = 0

while my_condition < 10: # esto es una caracteristica de Python - No utilizar if o elsif
    print(my_condition)
    my_condition += 2 # contador
else:
    print("Mi condicion es mayor o igual que 10")
    
print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break # esta funcion detiene la ejecucion del codigo una ves satisfecha la condicion
    print(my_condition)

print("La ejecucion continua")



## For ## nos sirve para iterar con un listado de elementos- esta atado a un nmero finito de datos.

my_list = [35, 24, 18 , 60, 17, 30, 30]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "vlad", "mano", "zam")

for element in my_tuple:
    print(element)

my_set = {"34", "1.70", "Vlad", "Mano"}

for element in my_set:
    print(element)

my_dict = {"Nombre" : "Vlad", "Apellido" : "Mano", "Edad" : 34, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad": 
        continue
    print("Se ejecuta")
    
else: # usando 'break' nos saltamos este else - al usar 'continue' se regresa al comienzo del 'for' y es obsoleto

    print("El bucle para diccionario ha finalizado")

# iteraciones ligadas a un conjunto de valores - "element es solo de ejemplo"

## Go-to ## >>>> no utilizar