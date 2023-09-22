# relacyjne bazy danych sql

import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')

    insert = '''
    INSERT INTO software (id,name,price) VALUES(1,'Python',100);

    '''

    select = '''
    SELECT * FROM software;
    '''

    update = '''
    UPDATE software SET price = 2000 WHERE id=1;
    '''

    delete = '''
    DELETE FROM software WHERE id=1;
    '''

    cursor = sql_connection.cursor()
    print("Baza danych została podłaczona")

    # cursor.execute(insert)
    # sql_connection.commit()

    for row in cursor.execute(select):
        print(row)  # (1, 'Python', 100.0)

    # cursor.execute(update)
    # sql_connection.commit()  # (1, 'Python', 2000.0)

    cursor.execute(delete)
    sql_connection.commit()

except sqlite3.Error as e:
    print("Bład podczas podłaczania bay danych", e)

finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych został zamknięta")

# 11:25 test
# 12:05
