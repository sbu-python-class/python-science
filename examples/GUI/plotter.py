#!/usr/bin/env python

# based on http://matplotlib.org/1.4.2/examples/user_interfaces/embedding_in_tk.html

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
    import tkFont
else:
    import tkinter as Tk
    import tkinter.font as tkFont


def str_to_f(str):
    a = parse_expr(str, evaluate=0)
    f = sympy.lambdify(x, a, "numpy")
    return f



class PlotterGUI:
    def __init__(self, parent):

        self.parent = parent
        
        myfont = tkFont.Font(size=14)

        self.frame_function = Tk.Frame(self.parent)
        self.frame_function.pack(fill=Tk.BOTH, expand=1)

        self.label = Tk.Label(self.frame_function, text="f(x) = ", font=myfont)
        self.label.grid(row=0, column=0, sticky=Tk.W)
        self.v = Tk.StringVar()
        self.func = Tk.Entry(self.frame_function, textvariable=self.v,
                             font=myfont)
        self.func.grid(row=0, column=1, sticky=Tk.W)

        self.frame_extrema = Tk.Frame(self.parent)
        self.frame_extrema.pack(fill=Tk.BOTH, expand=1)

        self.xmin_label = Tk.Label(self.frame_extrema, text="xmin: ",
                                   font=myfont)
        self.xmin_label.grid(row=0, column=0, sticky=Tk.W)
        self.xmin_v = Tk.StringVar()
        self.xmin = Tk.Entry(self.frame_extrema, textvariable=self.xmin_v,
                             font=myfont)
        self.xmin_v.set("0.0")
        self.xmin.grid(row=0, column=1, sticky=Tk.W)

        self.xmax_label = Tk.Label(self.frame_extrema, text="xmax: ",
                                   font=myfont)
        self.xmax_label.grid(row=0, column=2, sticky=Tk.W)
        self.xmax_v = Tk.StringVar()
        self.xmax = Tk.Entry(self.frame_extrema, textvariable=self.xmax_v,
                             font=myfont)
        self.xmax_v.set("1.0")
        self.xmax.grid(row=0, column=3, sticky=Tk.W)


        # a tk.DrawingArea
        self.f = Figure(figsize=(6,5), dpi=100)
        self.a = self.f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.f, master=self.parent)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        #toolbar = NavigationToolbar2TkAgg( canvas, root )
        #toolbar.update()
        #canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        self.frame_buttons = Tk.Frame(root)
        self.frame_buttons.pack(fill=Tk.BOTH, expand=1)

        self.plot_button = Tk.Button(self.frame_buttons, text='Plot',
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


        self.func.bind('<Return>', self._plot)
        self.xmin.bind('<Return>', self._plot)
        self.xmax.bind('<Return>', self._plot)
        # this allows the use of the enter key to plot the function as well 
        # while the cursor is in any one of the three text-entry fields

        
    def _plot(self, event=None):
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

plotter_gui = PlotterGUI(root)

root.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.


