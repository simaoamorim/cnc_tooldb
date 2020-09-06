#!/usr/bin/env python3
"""
CNC ToolDB application that manages a CNC Tool database.
"""
from sqlite3_handler import DB


def add_new_machine():
    """
    Add new machine
    """
    # Ask for machine name
    while True:
        machine_name = str(input('Machine name: '))
        if machine_name == '' or any(
                machine_name == ''
                or not char.isalnum()
                and not char.isspace()
                for char in machine_name):
            print('Invalid name')
            continue
        confirm = str(input(f"Set machine name to '{machine_name}'? (Y/n) "))
        if confirm.lower() == 'y' or confirm == '':
            try:
                db.add_machine(machine_name)
            except db.AlreadyExists as e:
                print(e)
                continue
            break


def print_machines():
    for row in db.get_machines():
        print(row)


if __name__ == '__main__':
    """Initialization steps for the application that are only executed on the
    main execution"""
    try:
        db = DB()
        add_new_machine()
        print_machines()
    except KeyboardInterrupt:
        pass
    exit(0)
