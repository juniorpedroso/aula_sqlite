import sqlite3

# Criando um banco de dados
banco = sqlite3.connect('primeiro_banco.db')

# Cria um objeto Cursor do banco de dados
cursor = banco.cursor()

Cria uma tabela de nome pessoas
cursor.execute('CREATE TABLE pessoas (nome text, idade integer, email text)')

Insere dados 
cursor.execute(
    'INSERT INTO pessoas VALUES("Maria", 40, "maria_123@gmail.com")')
cursor.execute('INSERT INTO pessoas VALUES("Joao", 20, "joao_123@gmail.com")')
cursor.execute('INSERT INTO pessoas VALUES("Aline", 33, "aline@gmail.com")')

# Grava as alterações
banco.commit()

# Visualiza o banco de dados
cursor.execute('SELECT * FROM pessoas')
print(cursor.fetchall())
