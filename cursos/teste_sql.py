import sqlite3

# Cria o banco
conn = sqlite3.connect('estoque.db')
cursor = conn.cursor()

# Cria tabela PES
cursor.execute('''
CREATE TABLE IF NOT EXISTS PES (
    material TEXT,
    lote TEXT,
    quantidade INTEGER
)
''')

# Insere dados de exemplo
dados = [
    ('MAT001', 'L123', 10),
    ('MAT001', 'L124', 15),
    ('MAT002', 'L125', 20),
    ('MAT002', 'L126', 25)
]

cursor.executemany('INSERT INTO PES VALUES (?,?,?)', dados)
conn.commit()

# TESTE: AVG funcionando
print("=== TESTE AVG ===")
resultado = cursor.execute('''
    SELECT material, AVG(quantidade) as media
    FROM PES 
    GROUP BY material
''').fetchall()

for row in resultado:
    print(f"Material: {row[0]} | Média: {row[1]}")

conn.close()
print("\n✅ Banco 'estoque.db' criado com sucesso!")