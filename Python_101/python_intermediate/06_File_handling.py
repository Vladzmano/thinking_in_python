### Tipos De ficheros - File handling ###

## .txt file ##

## Python_101 is the roor path
## using "r","w+","a", "rb",  we can read and write the file

import os

txt_file = open("Python_101/python_intermediate/06.1_my_file.txt", "w+") # leer y escribir / read adn write
txt_file.write("File Handling 101\nHello,\nPlease use this file wisely.\nThank you.")


#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline()) # lee primera
#print(txt_file.readline()) # lee segunda

for line in txt_file.readlines(): # lee tercera y cuarta linea.
    print(line)

txt_file.write("\nPS: Please bring water XOXOX")
print(txt_file.readline())

txt_file.close()

with open("Python_101/python_intermediate/06.1_my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

#os.remove("Python_101/python_intermediate/06.1_my_file.txt")



## .jason file ## Estos trabajan con elementos clave valor.

import json

json.dump

json_file = open("Python_101/python_intermediate/06.1_my_file.json", "w+")

json_test ={
    "name" : "Vlad", 
    "surname" : "Mano", 
    "age" : 34,
    "Languages" : ["Python", "Kotlin", "C#"],
    "website": "https://mysite.com"}

json.dump(json_test, json_file, indent= 2)

json_file.close() # para ver o leer el archivo por consola debemos cerra el archivo antes.

with open("Python_101/python_intermediate/06.1_my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


json_dict = json.load(open("Python_101/python_intermediate/06.1_my_file.json"))
print(json_dict)
print(type(json_dict)) # convertimos el archivo json a diccionario para trabajar con el.
print(json_dict["name"])


## .csv file ##

import csv

csv_file = open("Python_101/python_intermediate/06.1_my_file.csv", "w+")

csv_test ={
    "name" : "Vlad", 
    "surname" : "Mano", 
    "age" : 34,
    "Languages" : ["Python", "Kotlin", "C#"],
    "website": "https://mysite.com"}

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "laguages", "website"])
csv_writer.writerow(["vlad", "mano", 34, "python", "https://mywebite.com"])
csv_writer.writerow(["Jhon", "", 2, "Ruby", ""])


csv_file.close()


with open("Python_101/python_intermediate/06.1_my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)



## .xlsx file ##
# debe instalarse el modulo #

## .xlm file # para estructiracion de datos, configuracion.
# tambien requiere de un modulo 'pip install lxml'
import xml

xml_file = open("Python_101/python_intermediate/06.1_my_file.xml", "w+")