#!/usr/bin/python3
"
lists  all states from database hbtn_0e_0_usa
"
def print_state()
    import MySQLdb
    import sys
    var = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3],
                            charset="utf8")
    cursor = var.cursor()
    query = "SELECT id,name FROM states ORDER by states.id ASC"
    cursor.Execute(query)
    Rows = cursor.fetchall()
    for row in Rows:
        print(row)
    var.commit()
    cursor.close()
    var.close()
