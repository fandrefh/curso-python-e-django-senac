import sqlite3

conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

cursor.execute(
	"""
	CREATE TABLE cad_clientes (
		id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
		nome TEXT NOT NULL,
		idade INTEGER
	);

	"""
)
print("Banco e Tabela criados com sucesso!")
conn.close()