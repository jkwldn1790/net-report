#!/usr/bin/python

import psycopg2
from config import config

def insert_nettest(time, download, upload):
    sql = """INSERT INTO netresults(time, download, upload)
             VALUES(%s,%s,%s) RETURNING time;"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (time,download,upload))
        # get the generated id back
        time = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return time