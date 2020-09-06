#!/usr/bin/env python3
"""
Python module that handles the connection and actions to the local database
"""
import os.path
import sqlite3 as sql


class DB(object):
    def __init__(self, dbname='database.db'):
        """Initialize the connection to the database and, if it doesn't exist, create the necessary tables"""
        if os.path.isfile(dbname):
            self.db_exists = True
        else:
            self.db_exists = False
        self.conn = sql.connect(dbname)
        self.cur = self.conn.cursor()
        assert self.cur.connection == self.conn
        if not self.db_exists:
            self.init_db()

    def init_db(self):
        """Create the needed tables in the new database file"""
        self.cur.execute(
            '''
            CREATE TABLE machine (
                ID INTEGER PRIMARY KEY,
                name VARCHAR
            );
            '''
        )
        self.cur.execute(
            '''
            CREATE TABLE tool (
                ID INTEGER PRIMARY KEY,
                comment VARCHAR
            );
            '''
        )
        self.cur.execute(
            '''
            CREATE TABLE parameters (
                IDMachine INTEGER REFERENCES machine(ID)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                IDTool INTEGER REFERENCES tool(ID)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                comment VARCHAR,
                Offset_Z REAL,
                PRIMARY KEY (IDMachine, IDTool)
            );
            '''
        )
        self.conn.commit()

    def get_machines(self):
        return self.cur.execute("SELECT name FROM machine")

    def __del__(self):
        """Close the database connection and exit"""
        self.conn.close()
