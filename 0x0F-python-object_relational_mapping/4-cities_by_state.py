#!/usr/bin/python3
"""lists all cities from the database"""
import MySQLdb
import sys


def list_cities():
    var = MySQLdb.connect(host='localhost',
                          user=sys.argv[1],
                          passwd=sys.argv[2],
                          port=3306,
                          db=sys.argv[3])
    cursor = var.cursor()
    Query = """SELECT cities.id, cities.name, states.name FROM cities
               INNER JOIN states on cities.state_id = states.id ORDER
               by cities.id ASC"""
    cursor.execute(Query)
    ROWS = cursor.fetchall()
    for row in ROWS:
        print (row)
    cursor.close()
    var.close()


if __name__ == "__main__":
    list_cities()
