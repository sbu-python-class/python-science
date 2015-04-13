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
else:
    import tkinter as Tk

import tkFont

def str_to_f(str):
    a = parse_expr(str, evaluate=0)
    f = sympy.lambdify(x, a, "numpy")
    return f


def _plot():
    f_str = func.get()
    f = str_to_f(f_str)

    xm = float(xmin.get())
    xM = float(xmax.get())
    
    xv = np.linspace(xm, xM, 1000)
    fv = f(xv)

    a.plot(xv, fv)
    a.set_xlim([xm, xM])
    canvas.show()


def _clear():
    print "here"
    #f.clf(keep_observers=False)
    a.clear()
    canvas.draw()
    #canvas.get_tk_widget().destroy()
    #help(canvas)
    
    
def _quit():
    print func.get()
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    
root = Tk.Tk()
root.wm_title("plotter")


myfont = tkFont.Font(size=14)

frame1 = Tk.Frame(root)
frame1.pack(fill=Tk.BOTH, expand=1)

label = Tk.Label(frame1, text="f(x) = ", font=myfont)
label.grid(row=0, column=0, sticky=Tk.W)
v = Tk.StringVar()
func = Tk.Entry(frame1, textvariable=v, font=myfont)
func.grid(row=0, column=1, sticky=Tk.W)



frame_extrema = Tk.Frame(root)
frame_extrema.pack(fill=Tk.BOTH, expand=1)

xmin_label = Tk.Label(frame_extrema, text="xmin: ", font=myfont)
xmin_label.grid(row=0, column=0, sticky=Tk.W)
xmin_v = Tk.StringVar()
xmin = Tk.Entry(frame_extrema, textvariable=xmin_v, font=myfont)
xmin_v.set("0.0")
xmin.grid(row=0, column=1, sticky=Tk.W)

xmax_label = Tk.Label(frame_extrema, text="xmax: ", font=myfont)
xmax_label.grid(row=0, column=2, sticky=Tk.W)
xmax_v = Tk.StringVar()
xmax = Tk.Entry(frame_extrema, textvariable=xmax_v, font=myfont)
xmax_v.set("1.0")
xmax.grid(row=0, column=3, sticky=Tk.W)


# a tk.DrawingArea
f = Figure(figsize=(6,5), dpi=100)
a = f.add_subplot(111)
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

#toolbar = NavigationToolbar2TkAgg( canvas, root )
#toolbar.update()
#canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

frame2 = Tk.Frame(root)
frame2.pack(fill=Tk.BOTH, expand=1)

plot_button = Tk.Button(frame2, text='Plot', command=_plot, font=myfont)
plot_button.pack(side=Tk.BOTTOM)

clear_button = Tk.Button(frame2, text='Clear', command=_clear, font=myfont)
clear_button.pack(side=Tk.BOTTOM)

quit_button = Tk.Button(frame2, text='Quit', command=_quit, font=myfont)
quit_button.pack(side=Tk.BOTTOM)

plot_button.pack(side=Tk.LEFT, padx=5, pady=5)
clear_button.pack(side=Tk.LEFT, padx=5, pady=5)
quit_button.pack(side=Tk.RIGHT)


Tk.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.


