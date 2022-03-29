import pandas as pd
import mysql.connector as mysql

data = pd.read_excel('C:/Users/P8H61-M LX2/Documents/Visual Studio Code/Python/BCD/pizza-bcd-excel/PIZZAS2.xlsx')

#criando Banco de Dados
try:
    conn = mysql.connect(host='localhost', user='root', passwd='')
    if conn.is_connected():
        cursor = conn.cursor()

        cursor.execute("CREATE DATABASE PIZZARIA")
        print('database criada!')

except:
    print('erro: database não criada!')

#criando tabelas
if conn.is_connected():
    cursor.execute("USE PIZZARIA")
    record = cursor.fetchone()
    print("você está conectado à database PIZZARIA!", record)

    cursor.execute("CREATE TABLE CARDAPIO"
                    "(IDPIZZA int primary key auto_increment,"
                    " SABOR varchar(30) not null,"
                    " TAMANHO char(1) not null,"
                    " VALOR decimal(5,2) not null);")

    print("tabela criada!")

#inserir dados na tabela

    for i, row in data.iterrows():
        sql = "INSERT INTO CARDAPIO(IDPIZZA, SABOR, TAMANHO, VALOR)" \
              "VALUES('default', %s, %s, %s);"
        cursor.execute(sql, tuple(row))
        print('Dados inseridos!!!')

conn.commit()
conn.close()