import psycopg2
 
config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = 'Az09hg_tankist',
    user = 'postgres'
)

config.autocommit = True
cursor = config.cursor()

sql = '''SELECT * from phonebook where name LIKE '%i%' '''

cursor.execute(sql)

for i in cursor.fetchall():
    print(*i)

config.commit()
config.close()