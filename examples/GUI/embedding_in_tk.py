#!/usr/bin/env python

# based on http://matplotlib.org/1.4.2/examples/user_interfaces/embedding_in_tk.html

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import numpy as np

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

root = Tk.Tk()
root.wm_title("Embedding in TK")


f = Figure(figsize=(5,4), dpi=100)
a = f.add_subplot(111)
t = np.arange(0.0,3.0,0.01)
s = np.sin(2*np.pi*t)

a.plot(t,s)


# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

#toolbar = NavigationToolbar2TkAgg( canvas, root )
#toolbar.update()
#canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = Tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tk.BOTTOM)

Tk.mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.


