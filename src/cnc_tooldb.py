#!/usr/bin/env python3
"""
CNC ToolDB application that manages a CNC Tool database.
"""
from sqlite3_handler import DB

if __name__ == '__main__':
    """Initialization steps for the application that are only executed on the
    main execution"""
    db = DB()
    name = str(input('Machine name: '))
    db.add_machine(name)
    for row in db.get_machines():
        print(row)
    exit(0)
