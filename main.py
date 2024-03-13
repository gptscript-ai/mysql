import os
import argparse
import pymysql

from sqlalchemy import (
    URL,
    create_engine,
)

from llama_index.core import SQLDatabase
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.llms.openai import OpenAI


defaults = {
    "api_key": os.getenv("OPENAI_API_KEY"),
}

llm = OpenAI(
    api_key=defaults["api_key"],
)


def main():
    parser = argparse.ArgumentParser(description='Execute SQL query against a MySQL database')
    parser.add_argument('--query', required=True, help='SQL query to execute')
    args = parser.parse_args()

    username = os.environ["DB_USER"]
    password = os.environ["DB_PASS"]
    host = os.environ["DB_HOST"]
    port = int(os.environ["DB_PORT"])
    database = os.environ["DB_NAME"]

    # connect to DB, create engine
    connection_url = URL.create(
        "mysql+pymysql",
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
    )
    engine = create_engine(connection_url)

    sql_database = SQLDatabase(engine)

    query_engine = NLSQLTableQueryEngine(
        sql_database=sql_database, llm=llm
    )
    response = query_engine.query(args.query)

    print(response)


if __name__ == "__main__":
    main()
