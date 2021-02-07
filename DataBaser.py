import sqlite3

#criando conexao
conn = sqlite3.connect('userData.db')

#variaveis
cursor = conn.cursor()

#executa um comando sql
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
)
""");

print("Conectado ao Banco de Dados")