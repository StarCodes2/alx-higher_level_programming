#!/usr/bin/python3
"""lists all cities from a database.
   Usage: ./1-filter_states.py <mysql username>
                               <mysql password>
                               <database name>
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
                FROM cities AS c \
                JOIN states AS s \
                ON c.state_id = s.id \
                ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
