import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# lendo os dados
cursor.execute("""
SELECT * FROM cad_clientes;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()