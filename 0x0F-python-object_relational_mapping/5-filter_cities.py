#!/usr/bin/python3
""" takes in the name of a state as an argument and lists
    all cities of that state"""
import MySQLdb
import sys


def filter_cities():
    var = MySQLdb.connect(host='localhost',
                          port=3306,
                          user=sys.argv[1],
                          passwd=sys.argv[2],
                          db=sys.argv[3])
    cursor = var.cursor()
    state = sys.argv[4]
    Query = """SELECT cities.name FROM cities INNER JOIN
               states ON cities.state_id = states.id WHERE
               states.name = '{:s}'""".format(state)
    cursor.execute(Query)
    ROWS = cursor.fetchall()
    city = ''
    count = 0
    for row in ROWS:
        if count == 0:
            city = ''.join(row)
            count += 1
        else:
            city = city + ', ' + ''.join(row)
    print (city)
    cursor.close()
    var.close()


if __name__ == "__main__":
    filter_cities()
