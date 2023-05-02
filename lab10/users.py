import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    dbname = "postgres",
    user = "postgres",
    password = "Az09hg_tankist")

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    level INTEGER NOT NULL,
    score INTEGER NOT NULL);
""")

cur.execute("""
INSERT INTO users (username, level, score) 
VALUES ('Anuar', 0, 0), ('Altyn', 0, 0);
""")

conn.commit()

cur.close()
conn.close()