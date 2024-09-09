import sqlite3

connection = sqlite3.connect("events.db")
cursor = connection.cursor()

# Getting all the data
cursor.execute("SELECT * FROM events WHERE band='Tigers'")
data = cursor.fetchall()
print(data)

# Getting some the data
cursor.execute("SELECT band,city FROM events WHERE date='3.10.2024'")
data = cursor.fetchall()
print(data)

# Adding multiple data
new_data = [('Cats', 'Cat city', '5.10.2024'),
            ('snoop dog', 'Dog city', '5.10.2024')]
cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_data)
connection.commit()
