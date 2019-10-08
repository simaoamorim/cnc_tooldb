import wx
import wx.xrc
import wx.dataview


class MainFrame(wx.Frame):

    def __init__(self, parent, title=u"CNC ToolDB"):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=title, pos=wx.DefaultPosition,
                          size=wx.Size(600, 500), style=(wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL))
        self.SetSizeHints(wx.Size(600, 500), wx.DefaultSize)
        self.menu_bar = wx.MenuBar(0)
        self.file_menu = wx.Menu()
        # file_menu items
        self.file_menu_exit = wx.MenuItem(self.file_menu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL)
        self.file_menu_exit.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_QUIT, wx.ART_MENU))
        # self.file_menu_new = wx.MenuItem(self.file_menu, wx.ID_ANY, u"New", u"Create new file", wx.ITEM_NORMAL)
        # self.file_menu_new.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_MENU))
        # file_menu structure
        # self.file_menu.Append(self.file_menu_new)
        self.file_menu.AppendSeparator()
        self.file_menu.Append(self.file_menu_exit)

        self.help_menu = wx.Menu()
        # help_menu items
        self.help_menu_about = wx.MenuItem(self.help_menu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL)
        self.help_menu_about.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_HELP_SETTINGS, wx.ART_MENU))
        # help_menu structure
        self.help_menu.Append(self.help_menu_about)
        # menu_bar structure
        self.menu_bar.Append(self.file_menu, u"File")
        self.menu_bar.Append(self.help_menu, u"Help")
        self.SetMenuBar(self.menu_bar)

        b_sizer1 = wx.BoxSizer(wx.VERTICAL)
        b_sizer1.SetMinSize(wx.Size(400, 300))
        self.notebook = wx.Notebook(self)
        self.m_panel1 = wx.Panel(self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.notebook.InsertPage(0, self.m_panel1, 'Configuration')
        b_sizer9 = wx.BoxSizer(wx.VERTICAL)
        b_sizer4 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Machine:", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_RIGHT)
        self.m_staticText1.Wrap(0)
        b_sizer4.Add(self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)
        self.machine_chooser = wx.Choice(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                         [], wx.CB_SORT)
        self.machine_chooser.SetSelection(0)
        self.machine_chooser.SetMinSize(wx.Size(150, -1))
        b_sizer4.Add(self.machine_chooser, 0, wx.ALL | wx.EXPAND, 5)
        b_sizer4.Add((0, 0), 1, 0, 5)
        b_sizer9.Add(b_sizer4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.EXPAND, 5)
        b_sizer20 = wx.BoxSizer(wx.VERTICAL)
        self.config_control = wx.dataview.DataViewListCtrl(self.m_panel1,
                                                           wx.ID_ANY,
                                                           wx.DefaultPosition,
                                                           wx.DefaultSize,
                                                           wx.dataview.DV_HORIZ_RULES |
                                                           wx.dataview.DV_ROW_LINES |
                                                           wx.dataview.DV_VERT_RULES)
        self.config_control_tool_comment = self.config_control.AppendTextColumn(u"Tool",
                                                                                wx.dataview.DATAVIEW_CELL_EDITABLE, 200,
                                                                                wx.ALIGN_RIGHT,
                                                                                wx.dataview.DATAVIEW_COL_REORDERABLE |
                                                                                wx.dataview.DATAVIEW_COL_RESIZABLE |
                                                                                wx.dataview.DATAVIEW_COL_SORTABLE)
        self.config_control_tool_x_val = self.config_control.AppendTextColumn(u"X", wx.dataview.DATAVIEW_CELL_INERT,
                                                                              100,
                                                                              wx.ALIGN_CENTER,
                                                                              wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.config_control_tool_y_val = self.config_control.AppendTextColumn(u"Y", wx.dataview.DATAVIEW_CELL_INERT,
                                                                              100,
                                                                              wx.ALIGN_CENTER,
                                                                              wx.dataview.DATAVIEW_COL_RESIZABLE)
        self.config_control_tool_z_val = self.config_control.AppendTextColumn(u"Z", wx.dataview.DATAVIEW_CELL_INERT,
                                                                              100,
                                                                              wx.ALIGN_CENTER,
                                                                              wx.dataview.DATAVIEW_COL_RESIZABLE)
        b_sizer20.Add(self.config_control, 1, wx.ALL | wx.EXPAND, 0)
        b_sizer9.Add(b_sizer20, 1, wx.EXPAND, 0)
        self.m_panel1.SetSizer(b_sizer9)
        self.m_panel1.Layout()
        b_sizer9.Fit(self.m_panel1)
        b_sizer1.Add(self.notebook, 1, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(b_sizer1)
        self.Layout()
        self.Centre(wx.BOTH)

    def __del__(self):
        pass
