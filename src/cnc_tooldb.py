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
        with open('../version.txt', 'r') as version_file:
            self.info.SetVersion(version_file.read().__str__())
        self.info.SetName(u"CNC ToolDB")
        self.info.SetCopyright(u"Copyright (c) 2019 Simão Amorim <simao_amorim@outlook.pt>")
        with open('../LICENSE', 'r') as license_file:
            self.info.SetLicence(license_file.read().encode('UTF-8'))
        self.info.SetDevelopers([u"Simão Amorim (simao_amorim@outlook.pt)"])
        # Initialize the window
        super().__init__(parent=None, title=self.info.GetName()+" "+self.info.GetVersion())
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
        temp_id = event.GetId()
        if temp_id == self.machine_chooser.Id:
            print("Choice: %s" % self.machine_chooser.GetStringSelection())

    def menubar_handler(self, event):
        """Method to handle events from the menu bar in the main frame"""
        temp_id = event.GetId()
        if temp_id == self.file_menu_exit.Id:
            self.Destroy()
        elif temp_id == self.help_menu_about.Id:
            AboutBox(info=self.info, parent=self, )
        event.StopPropagation()


if __name__ == '__main__':
    """Initialization steps for the application that are only executed on the
    main execution"""
    root = wx.App(redirect=False)
    root.SetTopWindow(MainFrame())
    ret = root.MainLoop()
    print('GUI exit code: %d' % ret)
    print('Exiting')
    exit(0)
