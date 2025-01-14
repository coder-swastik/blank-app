import sqlite3


conn = sqlite3.connect('form_data.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM form_entries")
rows = cursor.fetchall()


for row in rows:
    print(row)


conn.close()
