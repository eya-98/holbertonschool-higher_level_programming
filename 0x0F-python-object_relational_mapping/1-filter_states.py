#!/usr/bin/python3
"""use of MySQLdb"""
import MySQLdb
import sys


def lists_states():
    var = MySQLdb.connect()
    cursor = var.cursor()
    Query = "SELECT * FROM STATES WHERE states.name like "N%"
    cursor.execute(query)
    rows = var.fetchall()
    for row in rows:
        print row
    cursor.close()
    var.close()

if __name__ == "__main__":
    lists_states()
