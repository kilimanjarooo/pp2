import psycopg2

config = psycopg2.connect(
    host = 'localhost', 
    database = 'postgres',
    user = 'postgres',
    password = 'Az09hg_tankist'
)

current = config.cursor()
#add values into table
id = 1
name = 'Anuar'
number = '+77772065850'

sql = '''
    INSERT INTO phonebook VALUES (%s, %s, %s); 
'''

current.execute(sql, (id, name, number))

current.close()
config.commit()
config.close()