import pandas as pd
import sqlite3
from datetime import datetime

TABLE_NAME = "stocks"

CREATE_TABLE = "CREATE TABLE %s (ticker text, date int, open real, high real, low real, close real)"

INSERT = "INSERT INTO stocks VALUES (\'{}\', strftime(\'%Y-%m-%d %H:%M:%S\', \'{}\'), {}, {}, {}, {})"

DELETE_TABLE = "DROP TABLE IF EXISTS %s"

SELECT_TICKER = f"SELECT * FROM {TABLE_NAME} where date >= '%s-%s-%s %s:%s:%s'"
# SELECT ticker, MIN(date) FROM stocks WHERE date >= '2021-04-08 17:40:00';
# select ticker, min(date) from stocks where date >= '2021-04-09 11:30:00' GROUP BY ticker;

# Queries server for latest price available as of the time specified.
#     The time query is expected to be in UTC time.
SELECT = "SELECT"


def execute(statement):
    """ Connect to database table and execute statement close connection
    """
    conn = sqlite3.connect(TABLE_NAME)
    df = pd.read_sql_query(statement, conn)
    return df


def insert(ticker, date, open, high, low, close):
    """ Insert data into table
    """
    # 2021-04-09 18:25:00
    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    execute(INSERT.format(ticker, date, open, high, low, close))


def create_table():
    """ Create table with table name
    """
    execute(CREATE_TABLE % (TABLE_NAME))


def delete():
    """ Drop the table
    """
    execute(DELETE_TABLE % TABLE_NAME)


def select_price(year, month, day, hour, minute):
    year = str(year)
    if len(str(month)) == 1:
        month = '0' + str(month)
    if len(str(day)) == 1:
        day = '0' + str(day)
    if len(str(hour)) == 1:
        hour = '0' + str(hour)
    if len(str(minute)) == 1:
        minute = '0' + str(minute)
    execute(SELECT_TICKER % (year, month, day, hour, minute))