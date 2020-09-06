#!/usr/bin/env python3
"""
Persistent data handler.

Defines the needed transactions to the local database, with simple
data validation.
"""
import os.path
import sqlite3 as sql


class DB(sql.Connection):
    """
    Database access object for persistent tool data storage.

    Allows multiple machine and tool definitions, able to set values
    for each possible combination of (machine, tool).

    E.g. tool #123 can have values set for machines _A_ and _B_, simultaneously.
    """
    def __init__(self, dbname='database.db'):
        """
        Initialize the connection to the database.

        If the specified one doesn't exist (including the default 'database.db'),
        a new one will be created and initialized with the required table
        structure.
        """
        if os.path.isfile(dbname):
            self.isNew = False
        else:
            self.isNew = True
        super().__init__(dbname)
        self.conn = self
        if self.isNew:
            self.init_db()

    def add_machine(self, name: str):
        """
        Insert a new machine definition into the database.

        The machine ID is automatically set by the SQLite autoincrement feature.
        """
        if name == '':
            raise ValueError
        try:
            self.conn.execute(
                "INSERT INTO machine(name) VALUES (:name);",
                {'name': name}
            )
        except self.IntegrityError:
            raise self.AlreadyExists("Machine '%s' already exists" % name)
        self.conn.commit()  # Save changes to file

    def get_machines(self):
        """
        Get list of machines saved in the database
        """
        return self.conn.execute("SELECT name FROM machine;")

    def __del__(self):
        """
        Close the database connection on object deletion
        """
        self.conn.close()

    def init_db(self):
        """
        Initialize database with the needed tables.

        Tables 'machine', 'tool' and 'parameters' are generated,
        with the configuration described in docs/db/cnc_tooldb_schema.svg
        """
        self.conn.execute(
            '''
            CREATE TABLE machine (
                name VARCHAR PRIMARY KEY
            );
            '''
        )
        self.conn.execute(
            '''
            CREATE TABLE tool (
                ID INTEGER PRIMARY KEY,
                comment VARCHAR
            );
            '''
        )
        self.conn.execute(
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
        # Need to use commit() to persistently save changes.

    class AlreadyExists(BaseException):
        pass
