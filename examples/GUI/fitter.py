#!/usr/bin/env python

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy as np

import sympy
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
    import tkFont as font
else:
    import tkinter as Tk
    from tkinter import font


def str_to_f(str):
    a = parse_expr(str, evaluate=0)
    f = sympy.lambdify(x, a, "numpy")
    return f


class FitterGUI:
    def __init__(self, parent):

        self.parent = parent
        
        myfont = font.Font() #size=14)

        # data file
        
        self.frame_data = Tk.Frame(self.parent, relief=Tk.SUNKEN, borderwidth=1)
        self.frame_data.pack(fill=Tk.BOTH, expand=1, ipadx=5, ipady=5)
        
        self.dlabel = Tk.Label(self.frame_data, text="data", font=myfont, fg="red")
        self.dlabel.grid(row=0, column=0, sticky=Tk.W, padx=5)

        self.file_label = Tk.Label(self.frame_data, text="file: ", font=myfont)
        self.file_label.grid(row=1, column=0, sticky=Tk.W, padx=5, ipadx=15)


        # fitting function
        
        self.frame_func = Tk.Frame(self.parent, relief=Tk.SUNKEN, borderwidth=1)
        self.frame_func.pack(fill=Tk.BOTH, expand=1, ipadx=5, ipady=5)
        
        self.flabel = Tk.Label(self.frame_func, text="fitting function", font=myfont, fg="red")
        self.flabel.grid(row=0, column=0, sticky=Tk.W, padx=5)


        # # a tk.DrawingArea
        
        self.f = Figure(figsize=(7,7), dpi=100)
        self.a = self.f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.f, master=self.parent)
        self.canvas.show()
        self.canvas.get_tk_widget().pack()
        

        # button bar
        
        self.frame_buttons = Tk.Frame(root)
        self.frame_buttons.pack(fill=Tk.BOTH, expand=1)

        self.plot_button = Tk.Button(self.frame_buttons, text='Fit',
                                     command=self._plot, font=myfont)
        self.plot_button.pack(side=Tk.BOTTOM)

        self.clear_button = Tk.Button(self.frame_buttons, text='Clear',
                                      command=self._clear, font=myfont)
        self.clear_button.pack(side=Tk.BOTTOM)

        self.quit_button = Tk.Button(self.frame_buttons, text='Quit',
                                     command=self._quit, font=myfont)
        self.quit_button.pack(side=Tk.BOTTOM)

        self.plot_button.pack(side=Tk.LEFT, padx=5, pady=5)
        self.clear_button.pack(side=Tk.LEFT, padx=5, pady=5)
        self.quit_button.pack(side=Tk.RIGHT)
        
        
    def _plot(self):
        f_str = self.func.get()
        f = str_to_f(f_str)

        xm = float(self.xmin.get())
        xM = float(self.xmax.get())
    
        xv = np.linspace(xm, xM, 1000)
        fv = f(xv)

        self.a.plot(xv, fv)
        self.a.set_xlim([xm, xM])
        self.canvas.show()


    def _clear(self):
        self.a.clear()
        self.canvas.draw()
    
    
    def _quit(self):
        self.parent.quit()     # stops mainloop

        # this is necessary on Windows to prevent Fatal Python Error:
        # PyEval_RestoreThread: NULL tstate
        self.parent.destroy()  

    
root = Tk.Tk()
root.wm_title("plotter")

plotter_gui = FitterGUI(root)

root.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.


