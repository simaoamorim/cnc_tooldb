# CNCToolDB

**CNCToolDB** allows you to store information about the tools you use <br>
on your CNC machines and then export a list of desired tools to <br>
automatically update the tool table on the CNC machine. <br>

# WARNING

**This README is outdated, please be patient as I will update it
as soon as I can.**

# Installation

This tool is written in Python so all you need to start using this tool the <br>
Python3 interpreter. Please visit www.python.org/downloads to know more <br>
on how to install it on your machine.

Python uses modules to expand its functionaliity. If you would like to know <br>
more about python modules take a look at [the python documentation].

## Python Dependencies

You can use the [pip] package manager to install python modules on <br>
your system. The required modules for this applications are located at <br>
[docs/requirements.txt].

### Install using pip

Start by changing into the docs folder with `cd docs/` and then:

If ***you have superuser rights*** run:
```bash
sudo pip install -r requirements.txt
```

If ***you don't***, then run:
```bash
pip install -r requirements.txt --user
```

The `--user` option makes **pip** install the modules only for the current <br>
user. If you need to use the application as different users on the same <br>
machine, you should install the modules on the system ***with superuser <br>
rights***.

# Usage

After [installing all dependencies], just change to the src/ directory with <br>
`cd src/` and start the program with
```bash
python3 cnc_tooldb.py
```

As an alternative, you can make sure the script is executable by issuing <br>
```bash
chmod +x cnc_toolbd.py
```
and then you can start it as a regular app with <br>
```bash
./cnc_toolbd.py
```
or by double-clicking it on your <br>
favourite file manager.

# Planed future features

The most important feature that is going to be developed in future <br>
releases is support for a connection with a [postgresql] database. <br>

A local [SQLite] database will always be the default way to store <br>
the data, but being able to synchronize with a remote server, <br>
sounds good to anyone who would like to use this program in <br>
several machines and keep all of them with the same information.

# Contributing

***This project is open-source and all contributions are welcome!***

## Bug's

If you found a bug in the code, please open a new issue. If you know <br>
how to fix it, then [fork] this repository,
make the necessary changes and <br>
create a [new pull request] with your fixed code.

## New Features



# License

This project and all the files in this repository are licensed under the <br>
**MIT** license. For more information please refer to the <br>
[/LICENSE](/LICENSE) file.

[docs/requirements.txt]: /docs/requirements.txt
[pip]: https://pip.pypa.io/en/stable/
[fork]: https://guides.github.com/activities/forking/
[new pull request]: https://help.github.com/en/articles/creating-a-pull-request-from-a-fork
[postgresql]: www.postgresql.org
[SQLite]: https://sqlite.org/
[installing all dependencies]: #python-dependencies
[the python documentation]: https://docs.python.org/3/tutorial/modules.html
