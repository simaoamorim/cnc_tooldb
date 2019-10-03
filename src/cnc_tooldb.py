#!/usr/bin/env python3
"""
File Docstring
"""
import wx
import wx.xrc


class App(wx.App):
    """
        Main application class. Here are defined all the methods and
        functions that control the entire application
    """
    def __init__(self, **argv):
        """Initialize the GUI from the XRC file, import the needed objects and declare variables"""
        super().__init__(**argv)
        # Get the main objects from XRC
        self.res = wx.xrc.XmlResource(filemask="wxformsbuilder/gui.xrc")
        self.MainFrame = self.res.LoadFrame(parent=None, name='MainFrame')
        self.SetTopWindow(self.MainFrame)
        self.machine_chooser = wx.xrc.XRCCTRL(window=self.MainFrame, str_id='machine_chooser')
        # Declare future variables
        self.machines = None
        # Call initialization methods
        self.init_binds()
        self.MainFrame.Show()

    def init_binds(self):
        """Bind GUI events to the proper methods"""
        self.MainFrame.Bind(wx.EVT_MENU, self.menu_exit, id=wx.xrc.XRCID(str_id='file_menu_exit'))

    def menu_exit(self, event):
        event.StopPropagation()
        print('Exiting application...')
        self.ExitMainLoop()


if __name__ == '__main__':
    root = App(redirect=False)
    ret = root.MainLoop()
    print('GUI exit code: %d' % ret)
    print('Exiting')
    exit(0)
