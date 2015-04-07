#!/usr/bin/env python

# based on http://matplotlib.org/1.4.2/examples/user_interfaces/embedding_in_tk.html

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import numpy as np

import sympy
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

root = Tk.Tk()
root.wm_title("plotter")


frame1 = Tk.Frame(root)
frame1.pack()

Tk.Label(frame1, text="f(x) = ").grid(row=0, column=0, sticky=Tk.W)
v = Tk.StringVar()
func = Tk.Entry(frame1, textvariable=v)
func.grid(row=0, column=1, sticky=Tk.W)


# a tk.DrawingArea
f = Figure(figsize=(5,4), dpi=100)
a = f.add_subplot(111)
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

#toolbar = NavigationToolbar2TkAgg( canvas, root )
#toolbar.update()
#canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


def str_to_f(str):
    a = parse_expr(str, evaluate=0)
    f = sympy.lambdify(x, a, "numpy")
    return f


def _plot():
    f_str = func.get()
    f = str_to_f(f_str)

    xv = np.linspace(0, 1, 1000)
    fv = f(xv)

    a.plot(xv, fv)
    canvas.show()

def _quit():
    print func.get()
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

frame2 = Tk.Frame(root)
frame2.pack(fill=Tk.BOTH, expand=1)

plot_button = Tk.Button(frame2, text='Plot', command=_plot)
plot_button.pack(side=Tk.BOTTOM)

quit_button = Tk.Button(frame2, text='Quit', command=_quit)
quit_button.pack(side=Tk.BOTTOM)

plot_button.pack(side=Tk.LEFT, padx=5, pady=5)
quit_button.pack(side=Tk.RIGHT)


Tk.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.


