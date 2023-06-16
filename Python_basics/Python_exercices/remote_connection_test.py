# Reto #23: La base de datos haciando uso del lenguaje Python

# Reglas:

"""
 * Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente base de datos MySQL:
 * - Host: mysql-5707.dinaserver.com
 * - Port: 3306
 * - User: mouredev_read
 * - Password: mouredev_pass
 * - Database: moure_test
 * 
 * Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
 * - SELECT * FROM `challenges`
 *
 * Se pueden usar librerías para realizar la lógica de conexión a la base de datos.
 """

# Debemos asegurarnos de contar con el conector MySQL apropiado instalado en nuetro PC

import mysql.connector

connection = mysql.connector.connect(
    host="mysql-5707.dinaserver.com",  # Dirección IP o nombre del host de la DB remota
    port="3306", # Puerto correspondinte a la DB
    user="mouredev_read",  # Nombre de usuario para acceder a DB
    password="mouredev_pass",  # Contraseña para acceder a la DB
    database="moure_test",  # Nombre de DB
)

# A partir de acá se se muestran las acciones realizadas sobre DB


# Crear un objeto cursor para ejecutar consultas
cursor = connection.cursor()

# Ejecutar una consulta
cursor.execute(
    "SELECT * FROM `challenges`"
    )

""" Otros Ejemplos de consulta

cursor.execute("SELECT * FROM id, name `challenges`")
cursor.execute("SELECT * FROM name id as `challenges`")
cursor.execute("SELECT * FROM `challenges`")
cursor.execute("SELECT * FROM `challenges`")

"""

# Obtenemos los resultados de la consulta
results = cursor.fetchall()

# Imprime/mustra las consultas de la tabla
for row in results:
    print(row)

# Cierra el cursor
cursor.close()

# Termina la conexión ala DB
connection.close()

