import os
import pymysql
from sqlalchemy import URL, MetaData, create_engine, select

def get_schema_info(host: str, port: int, username: str, password: str, database: str):
    connection_url = URL.create(
        "mysql+pymysql",
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
    )
    engine = create_engine(connection_url)
    with engine.connect() as conn:

        metadata_obj = MetaData()
        metadata_obj.reflect(bind=engine)
        for table_name in metadata_obj.tables:
            print(f'table: {table_name}')
            for col in metadata_obj.tables[table_name].columns:
                print(f'column_in_table_{table_name}: {col.name} type: {col.type} primary_key: {col.primary_key}')
            stmt = select(metadata_obj.tables[table_name]).limit(3)
            for row in conn.execute(stmt):
                print(f'example_entry_in_table_{table_name}: {row}')



if __name__ == "__main__":

    # Pull env vars
    username = os.environ["DB_USER"]
    password = os.environ["DB_PASS"]
    hostname = os.environ["DB_HOST"]
    port = int(os.environ["DB_PORT"])
    database = os.environ["DB_NAME"]

    get_schema_info(hostname, port, username, password, database)
