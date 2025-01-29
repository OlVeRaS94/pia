import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Crear tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER
    )
''')

# Insertar datos
usuarios = [('Ana', 25), ('Luis', 17), ('Marta', 30)]
cursor.executemany('INSERT INTO Usuarios (nombre, edad) VALUES (?, ?)', usuarios)
conn.commit()

# Consultar
cursor.execute('SELECT * FROM Usuarios WHERE edad > 18')
resultados = cursor.fetchall()
print("Usuarios mayores de 18:", resultados)

conn.close()