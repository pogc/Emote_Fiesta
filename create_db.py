import sqlite3
conn = sqlite3.connect("database.sqlite")
conn.execute('''CREATE TABLE emotes(
            ID PRIMARY KEY NOT NULL, 
            name TEXT NOT NULL, 
            url TEXT NOT NULL)''')
