# relacyjne bazy danych sql

import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')

    insert = '''
    INSERT INTO software (id,name,price) VALUES(1,'Python',100);
    
    '''
    cursor = sql_connection.cursor()
    print("Baza danych została podłaczona")

    cursor.execute(insert)
    sql_connection.commit()

except sqlite3.Error as e:
    print("Bład podczas podłaczania bay danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych został zamknięta")
