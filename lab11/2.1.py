import psycopg2 
from psycopg2 import Error

new_id, new_name, new_number = int(input()), input(), input() 

try:
    connection = psycopg2.connect( 
        host = 'localhost',  
        database = 'postgres', 
        user = 'postgres', 
        password = 'Az09hg_tankist' 
    ) 
 
    cursor = connection.cursor() 
    cursor.execute('CALL add_user(%s, %s, %s)', (new_id, new_name, new_number)) 
    connection.commit() 
 
except (Exception, Error) as error: 
    print("ERROR", error) 
finally: 
    if connection: 
        cursor.close() 
        connection.close()