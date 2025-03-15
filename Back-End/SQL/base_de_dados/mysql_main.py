import os

import pymysql  # type: ignore
import dotenv  # type: ignore

TABLE_NAME = 'customers'

# carrega o arquivo .env automaticamente se ele estiver com o nome .env
dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',

)

if __name__ == '__main__':

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                f'''
                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INT NOT NULL AUTO_INCREMENT,
                nome VARCHAR(50) NOT NULL,
                idade INT NOT NULL,
                PRIMARY KEY (id)
                );
                '''
            )
        connection.commit()

        with connection.cursor() as cursor:
            result = cursor.execute(
                f'''
                INSERT INTO {TABLE_NAME} (nome, idade)
                VALUES
                ("Vitor", 30),
                ("Paula", 25),
                ("Maria", 35),
                ("Joana", 40);
                '''
            )
            cursor.execute(
                f'TRUNCATE TABLE {TABLE_NAME}'
            )
            sql = f'''
            INSERT INTO {TABLE_NAME} (nome, idade)
            VALUES(
                %s,%s
            )
            '''
            cursor.executemany(
                sql,
                [
                    ('Vitor', 30),
                    ('Paula', 25),
                    ('Maria', 35),
                    ('Joana', 40)
                ]
            )
        connection.commit()

        with connection.cursor() as cursor:
            sql = f'''
                INSERT INTO {TABLE_NAME} (nome, idade) 
                VALUES (%(nome)s,%(idade)s)
            '''
            data2 = {
                'nome': 'Le',
                'idade': 30,
            }
            result = cursor.execute(sql, data2)
        connection.commit()

        with connection.cursor() as cursor:
            sql = f'''
                INSERT INTO {TABLE_NAME} (nome, idade) 
                VALUES (%(name)s,%(age)s)
            '''
            data3 = (
                {'name': 'Le', 'age': 30},
                {'name': 'Leandro', 'age': 27},
            )
            result = cursor.executemany(sql, data3)
        connection.commit()

        with connection.cursor() as cursor:
            sql = f'''
                INSERT INTO {TABLE_NAME} (nome, idade) 
                VALUES (%s,%s)
            '''
            data3 = (
                ('Murilo', 30),
                ('Zeze', 27),
            )
            result = cursor.executemany(sql, data3)
        connection.commit()
