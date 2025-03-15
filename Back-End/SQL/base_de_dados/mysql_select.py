from mysql_main import TABLE_NAME, connection


with connection:
    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME} WHERE id = 2'
        )
        cursor.execute(sql)

        data = cursor.fetchall()
        # for row in data:
        #     print(row)

    with connection.cursor() as cursor:
        # menor_id = input('Digite o menor id: ')
        # maior_id = input('Digite o maior id: ')
        menor_id = 1
        maior_id = 2

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s'
        )

        cursor.execute(sql, (menor_id, maior_id))
        # print(cursor.mogrify(sql, (menor_id, maior_id)))
        data2 = cursor.fetchall()

        # for row in data2:
        #     print(row)

    with connection.cursor() as cursor:

        sql = (
            f'DELETE FROM {TABLE_NAME} WHERE id = %s'
        )

        cursor.execute(sql, (1,))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME}')

        # for row in cursor.fetchall():
        #     print(row)

    # with connection.cursor() as cursor:
    #     cursor.execute("""
    #                    ALTER TABLE customers
    #                    DROP COLUMN email
    #                    """)
    #     connection.commit()

    with connection.cursor() as cursor:

        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id = %s'
        )

        cursor.execute(sql, ('Eleonor', 100, 3))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME}')

        for row in cursor.fetchall():
            print(row)
