#!/usr/bin/python3
"""use of MySQLdb"""
import MySQLdb
import sys


def lists_states():
    var = MySQLdb.connect(host='localhost',
                          port=3306,
                          user=sys.argv[1],
                          passwd=sys.argv[2],
                          db=sys.argv[3])
    cursor = var.cursor()
    Query = "SELECT* FROM states WHERE states.name like 'N%' ORDER BY id ASC"
    cursor.execute(Query)
    rows = cursor.fetchall()
    for row in rows:
        print (row)
    cursor.close()
    var.close()


if __name__ == "__main__":
    lists_states()
