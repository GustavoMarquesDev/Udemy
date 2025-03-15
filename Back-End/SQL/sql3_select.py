import sqlite3

from sql3_main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

# pega todos os registros da tabela com o fatchall
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

print('---')

cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = 2')
# pega um registro da tabela com o fetchone com o id  inserido, 2
row = cursor.fetchone()
_id, name, weight = row
print(_id, name, weight)

cursor.close()
connection.close()
