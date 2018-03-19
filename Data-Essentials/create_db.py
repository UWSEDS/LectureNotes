"""
Creates a database whose tables are CSV files. The database
file is created in the current directory.
Command line arguments:
  database time - a valid file name
  csvfile 1 - path to a csv file
  ...
  csvfile N - path to a csv file
"""

import argparse
import pandas as pd
import sqlite3 as sql
import sys

SIZE = 20000

parser = argparse.ArgumentParser(
    description="Create a SQL database from CSV files.")
parser.add_argument("dbname",
    help="Name of the database being created.")
parser.add_argument("csvfiles", nargs="+",
    help="Name of the CSV files in the database.")

dbname = sys.argv[1]
csvfiles = sys.argv[2:]

conn = sql.connect(dbname)
for csvfile in csvfiles:
  df = pd.read_csv(csvfile)
  columns = ['video_id', 'trending_date', 'publish_time']
  df = df.loc[0:SIZE, columns]
  table_name = csvfile.split('.')[0]
  df.to_sql(table_name, conn, if_exists="replace", index=False)

print("Database created!")
