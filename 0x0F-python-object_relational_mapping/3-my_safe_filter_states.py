#!/usr/bin/python3
"""lists all values in the states table where name matches the argument in a
   database(SQL injection protected).
   Usage: ./1-filter_states.py <mysql username>
                               <mysql password>
                               <database name>
                               <state name>
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * \
                FROM states \
                ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)

    cur.close()
    conn.close()
