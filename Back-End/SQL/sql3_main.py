import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)

# é o que faz a consulta no banco, exclui, altera, insere, etc
cursor = connection.cursor()

cursor.execute(
    f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL
    )
    '''
)

connection.commit()

sql = (
    f'''
    INSERT INTO {TABLE_NAME} (name, weight)
    VALUES (:nome, :peso)
    '''
)


if __name__ == '__main__':

    # limpa a tabela de ids fazendo começar do 1 novamente
    cursor.executescript(
        f'''
    DELETE FROM sqlite_sequence WHERE name = "{TABLE_NAME}";
    DELETE FROM {TABLE_NAME};
    '''
    )
    connection.commit()

    cursor.execute(sql, {'nome': 'Vitor', 'peso': 60})
    cursor.executemany(sql, (
        {'nome': 'Paula', 'peso': 90},
        {'nome': 'Maria', 'peso': 70},
        {'nome': 'Joana', 'peso': 60}
    ))
    connection.commit()

    # cursor.execute(f' DELETE FROM {TABLE_NAME} WHERE id = 2')
    # connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME} SET weight = 80, name = "locura" WHERE id = 3'
    )

    cursor.execute(
        f"""
        INSERT INTO {TABLE_NAME} (name, weight)
        VALUES ("João", 100)
        """
    )
    connection.commit()

    cursor.close()
    connection.close()
