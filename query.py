import os
import argparse
import pymysql


def execute_query(host, port, username, password, database, query):
    connection = pymysql.connect(host=host,
                                 port=port,
                                 user=username,
                                 password=password,
                                 database=database,
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            cursor.execute(query)

            results = cursor.fetchall()
            for row in results:
                print(row)

    finally:
        connection.close()


if __name__ == "__main__":
    username = os.environ["DB_USER"]
    password = os.environ["DB_PASS"]
    hostname = os.environ["DB_HOST"]
    port = int(os.environ["DB_PORT"])
    database = os.environ["DB_NAME"]

    parser = argparse.ArgumentParser(description='Execute SQL query against a MySQL database')
    parser.add_argument('--query', required=True, help='SQL query to execute')
    args = parser.parse_args()

    execute_query(hostname, port, username, password, database, args.query)
