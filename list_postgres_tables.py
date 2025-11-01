#!/usr/bin/env python3
"""
Script to connect to PostgreSQL database and export table list to a text file.
"""

import psycopg2
from psycopg2 import Error
import sys


def get_database_tables(host, database, user, password, port=5432):
    """
    Connect to PostgreSQL database and retrieve list of tables.

    Args:
        host (str): Database host address
        database (str): Database name
        user (str): Database user
        password (str): Database password
        port (int): Database port (default: 5432)

    Returns:
        list: List of table names
    """
    connection = None
    tables = []

    try:
        # Establish connection
        print(f"Connecting to PostgreSQL database '{database}' at {host}:{port}...")
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )

        # Create cursor
        cursor = connection.cursor()

        # Query to get all tables in public schema
        query = """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            AND table_type = 'BASE TABLE'
            ORDER BY table_name;
        """

        cursor.execute(query)
        tables = [row[0] for row in cursor.fetchall()]

        print(f"Successfully retrieved {len(tables)} tables.")
        cursor.close()

    except Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        sys.exit(1)

    finally:
        if connection:
            connection.close()
            print("Database connection closed.")

    return tables


def write_tables_to_file(tables, output_file="tables_list.txt"):
    """
    Write list of tables to a text file.

    Args:
        tables (list): List of table names
        output_file (str): Output file path
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("PostgreSQL Tables List\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Total tables: {len(tables)}\n\n")

            if tables:
                for idx, table in enumerate(tables, 1):
                    f.write(f"{idx}. {table}\n")
            else:
                f.write("No tables found in database.\n")

        print(f"Table list successfully written to '{output_file}'")

    except Exception as e:
        print(f"Error writing to file: {e}")
        sys.exit(1)


def main():
    """
    Main function to execute the script.
    """
    # Database configuration
    # You can modify these values or use environment variables
    DB_CONFIG = {
        'host': 'localhost',      # Database host
        'database': 'mydb',       # Database name
        'user': 'postgres',       # Database user
        'password': 'password',   # Database password
        'port': 5432              # Database port
    }

    # Output file path
    OUTPUT_FILE = 'tables_list.txt'

    print("=" * 50)
    print("PostgreSQL Table List Exporter")
    print("=" * 50)
    print()

    # Get tables from database
    tables = get_database_tables(**DB_CONFIG)

    # Write tables to file
    write_tables_to_file(tables, OUTPUT_FILE)

    print()
    print("=" * 50)
    print("Process completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
