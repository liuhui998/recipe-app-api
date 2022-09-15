"""
Django command to wait for the database to be available
"""

import time
import traceback
from sqlite3 import OperationalError  # noqa
from sys import stdout  # noqa
from psycopg2 import OperationalError as Psycopg2OpError  # noqa
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            # except (Psycopg2OpError, OperationalError):
            except Exception as e:
                self.stdout.write('Database unavailable, waiting 1 second...')
                self.stdout.write(traceback.format_stack())
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
