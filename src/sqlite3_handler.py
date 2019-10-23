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
        self.cur.execute('''CREATE TABLE machine (ID INTEGER PRIMARY KEY, name VARCHAR(100));''')
        self.cur.execute('''CREATE TABLE tool (ID INTEGER PRIMARY KEY, comment VARCHAR(100));''')
        self.cur.execute('''
                            CREATE TABLE parameters (
                                IDMachine INTEGER NOT NULL,
                                IDTool INTEGER NOT NULL,
                                comment VARCHAR(100),
                                Xval REAL,
                                Yval REAL,
                                Zval REAL,
                                FOREIGN KEY (IDMachine) REFERENCES machine(ID) ON UPDATE CASCADE ON DELETE CASCADE,
                                FOREIGN KEY (IDTool) REFERENCES tool(ID) ON UPDATE CASCADE ON DELETE CASCADE,
                                PRIMARY KEY (IDMachine, IDTool) 
                            );
                        ''')
        self.conn.commit()

    def get_machines(self, cur=None):
        if cur is None:
            cur = self.cur
        return cur.execute("""SELECT name FROM machine""")

    def get_machine_config(self, machine=None, cur=None):
        if machine is None:
            return None
        if cur is None:
            cur = self.cur
        return cur.execute(f"""SELECT tool.comment, parameters.Xval, 
                                parameters.Yval, parameters.Zval
                                FROM parameters
                                INNER JOIN machine ON parameters.IDMachine = machine.ID 
                                INNER JOIN tool ON parameters.IDTool = tool.ID
                                WHERE machine.name = '{machine}'""")

    def __del__(self):
        """Close the database connection and exit"""
        self.conn.close()
