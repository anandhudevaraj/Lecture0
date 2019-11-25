"""
Module to import a CSV file of 1000 book details and export them into a Postgres Database
"""
import csv
import os
import export_cred


DB_USER_NAME = os.getenv('DB_USER_NAME', None)
DB_PASSWORD = os.getenv('DB_PASSWORD', None)
DB_DATABASE = os.getenv('DB_DATABASE', None)
DB_PORT = os.getenv('DB_PORT', None)
DB_HOST = os.getenv('DB_HOST', None)
DB_URL = os.getenv('DB_URL', None)


# File name of books.csv, file is in same location as of import.py
books_csv = 'books.csv'


# Reading data from CSV file
with open(books_csv, 'r') as csv_file:
    # Creating a CSV reader object
    csv_reader = csv.reader(csv_file, delimiter=';')

    FIELDS = next(csv_reader)[:5]

    print(f"Fields are {FIELDS}")

    # Printing first 20 rows
    for row in list(csv_reader)[:20]:
        for key, col in zip(FIELDS, row[:5]):
            print(f"{key} : {col}", end=' ')
        print('\n')
