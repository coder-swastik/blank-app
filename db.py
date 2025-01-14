import sqlite3

conn = sqlite3.connect('form_data.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS form_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    course TEXT NOT NULL,
    gender TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("database and table created sucessfully")