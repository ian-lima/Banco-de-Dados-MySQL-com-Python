# criando tabela no banco de dados mysql
import mysql.connector

banco = mysql.connector.connect (
    host="localhost",
    user="root",
    password="",
    database="python_banco"
)

cursor = banco.cursor()

cursor.execute("CREATE TABLE pessoas (nome VARCHAR(255), idade INT(3), email VARCHAR(255))")