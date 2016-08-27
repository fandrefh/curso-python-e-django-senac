import sqlite3

conn = sqlite3.connect("clientes.db")

cursor = conn.cursor()


cursor.execute("""
INSERT INTO cad_clientes (nome, idade) VALUES ('Regis', 35);
""")

cursor.execute("""
INSERT INTO cad_clientes (nome, idade) VALUES ('Aloisio', 87);
""")

cursor.execute("""
INSERT INTO cad_clientes (nome, idade) VALUES ('Bruna', 21);
""")

cursor.execute("""
INSERT INTO cad_clientes (nome, idade) VALUES ('Matheus', 19);
""")

conn.commit()
print('Dados inseridos com sucesso.')
conn.close()