#!/usr/bin/env python3
"""
CNC ToolDB application manages a CNC Tool database using sqlite3
and wxPython for the GUI.
"""
import wx
import wx.dataview
import gui
from wx.adv import AboutBox, AboutDialogInfo
import sqlite3_handler as sql


class MainFrame(gui.MainFrame):
    """ Main application class. Here are defined all the methods and
        functions that control the entire application """
    def __init__(self):
        # Set info about the application
        self.info = AboutDialogInfo()
        self.info.SetName(f"CNC ToolDB")
        self.info.SetCopyright(f"Copyright (c) 2019 Simão Amorim <simao_amorim@outlook.pt>")
        with open(file=u"../version.txt", mode=u"r", encoding=u"UTF-8") as version_file:
            self.info.SetVersion(version_file.read())
        with open(file="../LICENSE", mode="r", encoding="UTF-8") as license_file:
            self.info.SetLicence(license_file.read())
        self.info.AddDeveloper(f"Simão Amorim (simao_amorim@outlook.pt)")
        # Initialize the window
        super().__init__(parent=None, title=f"{self.info.GetName()} {self.info.GetVersion()}")
        self.machine = None
        self.DB = sql.DB()
        self.init_binds()
        self.update_chooser()
        self.Show()

    def init_binds(self):
        """Bind GUI events to the appropriate handler methods"""
        self.Bind(wx.EVT_MENU, self.menubar_handler, self.menu_bar)
        self.Bind(wx.EVT_CHOICE, self.set_machine, self.machine_chooser)

    def update_chooser(self):
        for item in self.DB.get_machines():
            self.machine_chooser.Append(item)

    def set_machine(self, event):
        """Method to hande the choice of the machine"""
        event.StopPropagation()
        self.machine = self.machine_chooser.GetStringSelection()
        print(f"Choice: {self.machine}")
        self.update_config_table()

    def update_config_table(self):
        pass

    def menubar_handler(self, event):
        """Method to handle events from the menu bar in the main frame"""
        temp_id = event.GetId()
        if temp_id == self.file_menu_exit.Id:
            self.Destroy()
        elif temp_id == self.help_menu_about.Id:
            AboutBox(info=self.info, parent=self)
        event.StopPropagation()


if __name__ == '__main__':
    """Initialization steps for the application that are only executed on the
    main execution"""
    root = wx.App(redirect=False)
    root.SetTopWindow(MainFrame())
    ret = root.MainLoop()
    print(f"GUI exit code: {ret}")
    print(f"Exiting")
    exit(0)
