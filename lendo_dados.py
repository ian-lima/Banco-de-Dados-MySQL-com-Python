# lendo os dados na tabela mysql

import mysql.connector

banco = mysql.connector.connect (
    host="localhost",
    user="root",
    password="",
    database="python_banco"
)

cursor = banco.cursor()

comando_sql = "SELECT * FROM pessoas WHERE idade > 40"

cursor.execute(comando_sql)

valores_lidos = cursor.fetchall()

print(valores_lidos)