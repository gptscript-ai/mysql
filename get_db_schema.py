import os
import pymysql
import argparse

def get_schema_info(host: str, port: int, username: str, password: str, database: str):
    connection = pymysql.connect(host=host,
                                 port=port,
                                 user=username,
                                 password=password,
                                 database=database,
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()

            for table in tables:
                table_name = table['Tables_in_' + database]

                cursor.execute(f"SHOW COLUMNS FROM {table_name}")
                columns = cursor.fetchall()

                print(f"Table: {table_name}")
                print("Columns:")
                for column in columns:
                    print(f"\t{column['Field']} - {column['Type']}")
                print()

    finally:
        connection.close()

if __name__ == "__main__":

    # Pull env vars
    username = os.environ["DB_USER"]
    password = os.environ["DB_PASS"]
    hostname = os.environ["DB_HOST"]
    port = int(os.environ["DB_PORT"])
    database = os.environ["DB_NAME"]

    get_schema_info(hostname, port, username, password, database)
