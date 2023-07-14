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

#os.remove("Python_101/python_intermediate/06.1_my_file.txt")



## .jason file ## Estos trabajan con elementos clave valor.

import json

json.dump

json_file = open("Python_101/python_intermediate/06.1_my_file.json", "w+")

json_test ={
    "name" : "Vlad", 
    "surname" : "Mano", 
    "age" : 34,
    "Language" : "Python",
    "website": "https://mysite.com"}

json.dump(json_test, json_file, indent= 4)