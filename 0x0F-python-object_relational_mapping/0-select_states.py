#!/usr/bin/python3
"""
This script retrieves and displays the list of states from a MySQL database.
"""


import MySQLdb
import sys


def select_states(username, password, database_name):
    """
    Retrieve and display the list of states from the specified MySQL database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Name of the database.


    returns:
        None
    """
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cur.fetchall()
        for row in rows:
            print(row)

        
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))


    finally:
        cur.close()
        db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(sys.argv[0]))
        sys.exit(1)


    username = sys.argv[1]
    pasword = sys.argv[2]
    database_name = sys.argv[3]


    
