import sqlite3

# Connect to the database
conn = sqlite3.connect('form_data.db')
cursor = conn.cursor()

# Query the database
cursor.execute("SELECT * FROM form_entries")
rows = cursor.fetchall()

# Display the rows
for row in rows:
    print(row)

# Close the connection
conn.close()
