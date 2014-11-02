from contextlib import closing, contextmanager

from mysql import connector as mysql_connector
import psycopg2.pool

from demo import config

MYSQL_POOL = None
PGSQL_POOL = None


@contextmanager
def pgsql_pool_returner(cxn):
    try:
        yield cxn
    finally:
        PGSQL_POOL.putconn(cxn)


def mysql():
    global MYSQL_POOL

    if MYSQL_POOL is None:
        MYSQL_POOL = mysql_connector.pooling.MySQLConnectionPool(pool_name='mysql_pool', pool_size=10, **config.MYSQL_DSN)

    return closing(MYSQL_POOL.get_connection())


def pgsql():
    # return closing(psycopg2.connect(**config.PGSQL_DSN))
    global PGSQL_POOL

    if PGSQL_POOL is None:
        PGSQL_POOL = psycopg2.pool.SimpleConnectionPool(5, 10, **config.PGSQL_DSN)

    return pgsql_pool_returner(PGSQL_POOL.getconn())
