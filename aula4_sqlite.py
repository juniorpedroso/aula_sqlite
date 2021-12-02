import sqlite3

# Variáveis
nome = 'Juliana'
idade = 28
email = 'juliana@gmail.com'

# Criando um banco de dados
banco = sqlite3.connect('primeiro_banco.db')

# Cria um objeto Cursor do banco de dados
cursor = banco.cursor()

# Cria uma tabela de nome pessoas
# cursor.execute('CREATE TABLE pessoas (nome text, idade integer, email text)')

# Insere dados 
cursor.execute('INSERT INTO pessoas VALUES("'+nome+'","'+str(idade)+'", "'+email+'")')

# Grava as alterações
banco.commit()

# Visualiza o banco de dados
cursor.execute('SELECT * FROM pessoas')
print(cursor.fetchall())