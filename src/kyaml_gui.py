#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#    Aug 05, 2022 01:58:31 AM +03  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import kyaml_gui_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    style.configure('Vertical.TScrollbar',  background=_bgcolor,
        arrowcolor= _fgcolor)
    style.configure('Horizontal.TScrollbar',  background=_bgcolor,
        arrowcolor= _fgcolor)
    style.configure('Treeview',  font="TkDefaultFont")
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("589x503+308+122")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1,  1)
        top.title("Kyaml Note-taking assistant")
        top.configure(highlightcolor="black")

        self.top = top

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top, activebackground='beige'
                ,activeforeground='black', tearoff=0)
        self.menubar.add_cascade(label='Notes',menu=self.sub_menu,)
        self.sub_menu.add_command(label='New notes')
        self.sub_menu.add_command(label='Open a note')
        self.sub_menu.add_command(label='Save')
        self.sub_menu.add_command(label='Save as')
        self.sub_menu1 = tk.Menu(top, activebackground='beige'
                ,activeforeground='black', tearoff=0)
        self.menubar.add_cascade(label='Help',menu=self.sub_menu1,)
        self.sub_menu1.add_command(label='RTFM')
        self.sub_menu1.add_command(label='About')

        _style_code()
        self.Scrolledtreeview1 = ScrolledTreeView(self.top)
        self.Scrolledtreeview1.place(relx=0.0, rely=0.099, relheight=0.899
                , relwidth=1.0)
        self.Scrolledtreeview1.configure(columns="Col1 Col2")
        # build_treeview_support starting.
        self.Scrolledtreeview1.heading("#0",text="Title")
        self.Scrolledtreeview1.heading("#0",anchor="center")
        self.Scrolledtreeview1.column("#0",width="218")
        self.Scrolledtreeview1.column("#0",minwidth="20")
        self.Scrolledtreeview1.column("#0",stretch="1")
        self.Scrolledtreeview1.column("#0",anchor="w")
        self.Scrolledtreeview1.heading("Col1",text="Note")
        self.Scrolledtreeview1.heading("Col1",anchor="center")
        self.Scrolledtreeview1.column("Col1",width="220")
        self.Scrolledtreeview1.column("Col1",minwidth="20")
        self.Scrolledtreeview1.column("Col1",stretch="1")
        self.Scrolledtreeview1.column("Col1",anchor="w")
        self.Scrolledtreeview1.heading("Col2",text="TIme/Date")
        self.Scrolledtreeview1.heading("Col2",anchor="center")
        self.Scrolledtreeview1.column("Col2",width="137")
        self.Scrolledtreeview1.column("Col2",minwidth="20")
        self.Scrolledtreeview1.column("Col2",stretch="1")
        self.Scrolledtreeview1.column("Col2",anchor="w")

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.015, rely=0.02, height=33, width=33)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(compound='left')
        self.Button1.configure(text='''+''')

        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.085, rely=0.02, height=33, width=33)
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(borderwidth="2")
        self.Button2.configure(compound='left')
        self.Button2.configure(text='''-''')

        self.Button3 = tk.Button(self.top)
        self.Button3.place(relx=0.849, rely=0.02, height=33, width=33)
        self.Button3.configure(activebackground="beige")
        self.Button3.configure(borderwidth="2")
        self.Button3.configure(compound='left')
        self.Button3.configure(text='''???''')

        self.Button4 = tk.Button(self.top)
        self.Button4.place(relx=0.917, rely=0.02, height=33, width=33)
        self.Button4.configure(activebackground="beige")
        self.Button4.configure(borderwidth="2")
        self.Button4.configure(compound='left')
        self.Button4.configure(text='''???''')

        self.Button5 = tk.Button(self.top)
        self.Button5.place(relx=0.153, rely=0.02, height=33, width=43)
        self.Button5.configure(activebackground="beige")
        self.Button5.configure(borderwidth="2")
        self.Button5.configure(compound='left')
        self.Button5.configure(text='''???+''')

        self.Button6 = tk.Button(self.top)
        self.Button6.place(relx=0.238, rely=0.02, height=33, width=43)
        self.Button6.configure(activebackground="beige")
        self.Button6.configure(borderwidth="2")
        self.Button6.configure(compound='left')
        self.Button6.configure(text='''???-''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.374, rely=0.02, height=31, width=239)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(compound='left')
        self.Label1.configure(font="-family {DejaVu Sans} -size 10")
        self.Label1.configure(text='''Tip: Add \r \g \b to write in color''')

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
def start_up():
    kyaml_gui_support.main()

if __name__ == '__main__':
    kyaml_gui_support.main()




