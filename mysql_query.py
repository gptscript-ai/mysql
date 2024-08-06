import os
import sys
import pymysql

def eprint(s):
    print(s, file=sys.stderr)

def execute_query(host: str, port: int, username: str, password: str, database: str, query: str):
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

    query = os.environ["QUERY"]

    username = os.environ["DB_USER"]
    password = os.environ["DB_PASS"]
    hostname = os.environ["DB_HOST"]
    port = int(os.environ["DB_PORT"])
    database = os.environ["DB_NAME"]

    eprint("=========SQL QUERY=========")
    eprint(query)
    eprint("===========================")

    execute_query(hostname, port, username, password, database, query)
