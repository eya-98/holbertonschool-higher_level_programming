#!/usr/bin/python3
"""
lists  all states from database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def print_state():
    """print states"""
    var = MySQLdb.connect(host='localhost',
                          port=3306,
                          user=sys.argv[1],
                          passwd=sys.argv[2],
                          db=sys.argv[3])
    cursor = var.cursor()
    query = "SELECT id,name FROM states ORDER by states.id ASC"
    cursor.execute(query)
    Rows = cursor.fetchall()
    for row in Rows:
        print(row)
    cursor.close()
    var.close()

if __name__ == "__main__":
    print_state()
