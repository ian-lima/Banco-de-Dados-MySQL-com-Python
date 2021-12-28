# deletando os dados da tabela mysql

import mysql.connector

banco = mysql.connector.connect (
    host="localhost",
    user="root",
    password="",
    database="python_banco"
)

cursor = banco.cursor()

comando_sql = "DELETE FROM pessoas WHERE idade = 65"

cursor.execute(comando_sql)

banco.commit()