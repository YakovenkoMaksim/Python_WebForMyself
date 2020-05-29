import sqlite3


def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


db = sqlite3.connect('test_db.sqlite')
db.row_factory = dict_factory
cursor = db.cursor()

email = 'petrov@gmail.com'
# cursor.execute(f"SELECT * FROM users WHERE email = {email}") - never use!!!

# cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
# cursor.execute('SELECT * FROM users WHERE email = :email OR name = :name', {'email': email, 'name': 'John Doe'})

cursor.execute('SELECT * FROM users')
# res = cursor.fetchall()
# print(res)
# for user in res:
#     print(user['name'], user['email'])

cursor.execute("INSERT INTO users (name, email) VALUES ('User4', 'user4@gmail.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('User5', 'user5@gmail.com')")
db.total_changes
db.commit()

db.close()
