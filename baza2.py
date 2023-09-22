# relacyjne bazy danych sql

import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    query = '''
    CREATE TABLE developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);'''

    with open('tables.sql', 'r') as file:
        sql_script = file.read()

    cursor = sql_connection.cursor()
    print("Baza danych została podłaczona")

    # cursor.execute(query)  Tabela juz istnieje, komentujemy by nie wykonywac ponownie
    # sql_connection.commit()  # trwały zapis do bazy danych

    cursor.executescript(sql_script)

except sqlite3.Error as e:
    print("Bład podczas podłaczania bay danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych został zamknięta")