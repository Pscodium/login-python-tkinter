import sqlite3
from sqlite3 import Error


def ConnectDB():
    way='users.db'
    con=None
    try:
        con=sqlite3.connect(way)
    except Error as ex:
        print(ex)
    return con

vcon = ConnectDB()

def insert(connection, sql):
    try:
        c= connection.cursor()
        c.execute(sql)
        connection.commit()
        print('Registrado com SUCESSO')
    except Error as ex:
        print(ex)

def login(connection, sql):
    try:
        c= connection.cursor()
        c.execute(sql)
        connection.commit()
        res=c.fetchone()
        vcon.close()
        print('Usuário encontrado com SUCESSO')
    except Error as ex:
        print(ex)
    return res
        