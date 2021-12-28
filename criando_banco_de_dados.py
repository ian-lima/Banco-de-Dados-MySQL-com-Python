# criando banco de dados mysql

import mysql.connector

banco = mysql.connector.connect (
    host="localhost",
    user="root",
    password="",
)

cursor = banco.cursor()

cursor.execute("CREATE DATABASE python_banco")