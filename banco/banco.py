import sqlite3

banco = sqlite3.connect("econocom.db")
cursor = banco.cursor()

#cursor.execute('CREATE TABLE tb_pedidos (cliente_pedido text, produto_pedido text, quantidade_pedido integer)')

#cursor.execute("INSERT INTO tb_clientes VALUES('lucas', 1234)")
#banco.commit()

#cursor.execute('SELECT * FROM tb_clientes')
#print(cursor.fetchall())

#cursor.execute('DELETE FROM tb_clientes')
#banco.commit()

cursor.execute("SELECT * FROM tb_clientes")
dados = cursor.fetchall()
print(dados)
#banco.commit()