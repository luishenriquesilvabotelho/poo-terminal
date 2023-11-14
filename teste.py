import sqlite3 

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Jogos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Turma TEXT,
        Horario TEXT,
        Placar TEXT,
        Local TEXT
    )
''')