import mysql.connector

# Establecer la conexión
connection = mysql.connector.connect(
    host="mysql-5707.dinaserver.com",
    port= "3306",
    user="mouredev_read",
    password="mouredev_pass",
    database="moure_test"
)

# Crear un objeto cursor para ejecutar consultas
cursor = connection.cursor()

# Ejecutar una consulta SELECT
cursor.execute("SELECT * FROM `challenges`")

# Obtener los resultados de la consulta
results = cursor.fetchall()

# Recorrer los resultados
for row in results:
    print(row)

# Cerrar el cursor y la conexión
cursor.close()
connection.close()