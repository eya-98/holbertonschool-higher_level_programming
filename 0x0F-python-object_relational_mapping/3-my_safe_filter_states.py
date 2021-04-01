#!/usr/bin/python3
"""
displays all values in the states
table safe from MySQL injections!
"""
import sys
import MySQLdb


def display_values():
    var = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    cursor = var.cursor()
    word = sys.argv[4]
    cursor.execute("""SELECT id,name FROM states where name = %s
                ORDER by id ASC""", (word,))
    ROWS = cursor.fetchall()
    for row in ROWS:
        print(row)
    cursor.close()
    var.close()


if __name__ == "__main__":
    display_values()