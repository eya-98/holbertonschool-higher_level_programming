#!/usr/bin/python3
"""displays all values in the states"""
import sys
import MySQLdb


def display_values():
    """display value of searched state"""
    var = MySQLdb.connect(user=sys.argv[1],
                          passwd=sys.argv[2],
                          db=sys.argv[3],
                          port=3306,
                          host="localhost")
    cursor = var.cursor()
    word = sys.argv[4]
    query = """SELECT * FROM states WHERE states.name = '{:s}'
               ORDER by id ASC""".format(word)
    cursor.execute(query)
    ROWS = cursor.fetchallmy()
    for row in ROWS:
        print (row)
    cursor.close()
    var.close()


if __name__ == "__main__":
    display_values()
