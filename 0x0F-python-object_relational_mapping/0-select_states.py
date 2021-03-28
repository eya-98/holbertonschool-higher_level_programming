#!/usr/bin/python3
"""
lists  all states from database hbtn_0e_0_usa
"""


def print_state():
    """print states"""
    import MySQLdb
    import sys
    var = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3])
    cursor = var.cursor()
    query = "SELECT * FROM states ORDER by id ASC"
    cursor.execute(query)
    Rows = cursor.fetchall()
    for row in Rows:
        print(row)
    var.commit()
    cursor.close()
    var.close()

if __name__ == "__main__":
    print_state()
