import pytest
from django.db import connections
from django.test import Client
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import authenticate, login
from crm_auth.models import User

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def run_sql(sql):
    conn = psycopg2.connect(
        database='crm_db',
        user='postgres',
        password='postgres',
        host='127.0.0.1',
        port=5432
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql)
    conn.close()


@pytest.fixture(scope='session', autouse=True)
def django_db_setup():
    settings.DATABASES['default']['NAME'] = 'test_db'
    settings.DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'
    settings.DATABASES['default']['USER'] = 'postgres'
    settings.DATABASES['default']['PASSWORD'] = 'postgres'
    settings.DATABASES['default']['HOST'] = '127.0.0.1'
    settings.DATABASES['default']['PORT'] = 5432

    run_sql('DROP DATABASE IF EXISTS test_db')
    run_sql('CREATE DATABASE test_db TEMPLATE crm_db')


    yield

    for connection in connections.all():
        connection.close()

    run_sql('DROP DATABASE test_db')
