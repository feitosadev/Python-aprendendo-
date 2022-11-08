import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234567',
    database = 'bdcrudpython'
)

cursor = conexao.cursor()

#CRUD
#C
nome_produto = "todynho"
valor = 2
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()

#R
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

#U
nome_produto = "todynho"
valor = 3
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

#D
nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()