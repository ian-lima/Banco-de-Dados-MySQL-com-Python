# inserindo dados na tabela mysql

import mysql.connector

banco = mysql.connector.connect (
    host="localhost",
    user="root",
    password="",
    database="python_banco"
)

cursor = banco.cursor()

comando_sql = "INSERT INTO pessoas (nome, idade, email) VALUES (%s, %s, %s)"
dados = ("Fernanda", "64", "fernanda123@gmail.com")
cursor.execute(comando_sql, dados)

banco.commit()