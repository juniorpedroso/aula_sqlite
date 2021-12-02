import sqlite3

try:
    # Criando um banco de dados
    banco = sqlite3.connect('primeiro_banco.db')

    # Cria um objeto Cursor do banco de dados
    cursor = banco.cursor()

    # Apaga um dado
    cursor.execute('DELETE from pessoas WHERE nome = "Juliana"')

    # Grava as alterações
    banco.commit()
    banco.close()
    print('\nOs dados foram removidos com sucesso!\n')

except sqlite3.Error as erro:
    print('\nErro ao excluir: ', erro)
