"""app/lambda_function.py
"""

import os
import sys

import psycopg2


class Database():
    """Database
    """
    class Parameter():
        """Parameter
        """

        def __init__(self, host, port, dbname, table, user, password, query):
            self.host = host
            self.port = port
            self.dbname = dbname
            self.table = table
            self.user = user
            self.password = password
            self.query = query

    def __init__(self, param):
        self.db = param
        self.header = tuple()
        self.records = list()
        self.counts = int()

    def _connection(self):
        """_connection
        """
        print('connect to db: {}/{}'.format(self.db.host, self.db.dbname))
        return psycopg2.connect(
            host=self.db.host,
            port=self.db.port,
            dbname=self.db.dbname,
            user=self.db.user,
            password=self.db.password
        )

    def query(self):
        """query
        """
        with self._connection() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(self.db.query)
                    self.header = cursor.description
                    self.records = cursor.fetchall()
                    self.counts = len(self.records)
                except psycopg2.Error as e:
                    print(e)
                    sys.exit()
        return True


def lambda_handler(event, context):
    """lambda_handler
    """
    print('event: {}'.format(event))
    print('context: {}'.format(context))

    param = Database.Parameter(
        host=os.getenv('DB_HOST', ''),
        port=os.getenv('DB_PORT', ''),
        dbname=os.getenv('DB_DBNAME', ''),
        table=os.getenv('DB_TABLE', ''),
        user=os.getenv('DB_USER', ''),
        password=os.getenv('DB_PASSWORD', ''),
        query=os.getenv('DB_QUERY', '')
    )

    db = Database(param=param)
    db.query()

    return {
        'status_code': 200,
        'records': str(db.records),
        'counts': db.counts
    }


if __name__ == '__main__':
    print(lambda_handler(event=None, context=None))
