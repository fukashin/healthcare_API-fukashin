#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import time
import psycopg2
from django.core.management import execute_from_command_line
from psycopg2 import OperationalError


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "healthcare_API.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    def wait_for_db():
        retry_count = 0
        max_retries = 5
        while retry_count < max_retries:
            try:
                # データベースに接続を試みる
                conn = psycopg2.connect(
                    dbname="healthcare_db",
                    user="admin",
                    password="admin",
                    host="db",
                    port="5432"
                )
                conn.close()
                print("Database connection successful.")
                return
            except OperationalError:
                retry_count += 1
                print(f"Database connection failed. Retrying in 5 seconds... (Attempt {retry_count}/{max_retries})")
                time.sleep(5)
        print("Database connection could not be established. Exiting.")
        exit(1)


if __name__ == "__main__":
    main()
    # execute_from_command_line()
