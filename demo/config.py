import os

MYSQL_DSN = {
    'user': os.getenv('DEMO_MYSQL_USER', 'test'),
    'password': os.getenv('DEMO_MYSQL_PASSWORD', 'test'),
    'host': os.getenv('DEMO_MYSQL_HOST', 'localhost'),
    'database': os.getenv('DEMO_MYSQL_DB', 'test'),
}

PGSQL_DSN = {
    'user': os.getenv('DEMO_PGSQL_USER', 'test'),
    'password': os.getenv('DEMO_PGSQL_PASSWORD', 'test'),
    'host': os.getenv('DEMO_PGSQL_HOST', '127.0.0.1'),
    'database': os.getenv('DEMO_PGSQL_DB', 'test'),
}
