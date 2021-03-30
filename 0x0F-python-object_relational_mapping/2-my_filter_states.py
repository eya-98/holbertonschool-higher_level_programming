#!/usr/bin/python3
"""displays all values in the states"""
import sys
import MySQLdb


def display_value():
    var = MySQLdb.connect(user=sys.argv[1],
                          passwd=sys.argv[2],
                          db=sys.argv[3],
                          port=3306,
                          host="localhost")
    cursor = var.cursor()
    word = sys.argv[4]
    Query = """SELECT * FROM states WHERE states.name = '{:s}'
            ORDER by id ASC""".format(word)
    cursor.execute(Query)
    ROWS = cursor.fetchall()
    for row in ROWS:
        print (row)
    cursor.close()
    var.close()

    if __name__ == "__main__":
        display_value()
