import sqlite3

connection = sqlite3.connect('guestbook.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

c = connection.cursor()

c.execute("""
SELECT datetime FROM post
""");

query = c.fetchone()
print(query[0])
print(len(query))

connection.close()
