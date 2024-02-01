import pymysql
from pymysql import DatabaseError
from decouple import config

def db_connection():
    try:
        return pymysql.connect(
            host=config('MYSQL_HOST'),
            user=config('MYSQL_USER'),
            password=config('MYSQL_PASSWORD'),
            database=config('MYSQL_DATABASE'),
            port=int(config('MYSQL_PORT'))
        )
    except DatabaseError as error:
        raise error
