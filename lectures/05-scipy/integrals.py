import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def f(x):
    """ the function we are integrating """
    return 1.0 + x*0.25*np.sin(np.pi*x)


plt.rcParams.update({'xtick.labelsize': 18,
                     'ytick.labelsize': 18,
                     'text.fontsize': 18})



N_fine = 200
N_bins = 3

xmin = -0.5
xmax = 2.5

x = np.linspace(xmin, xmax, N_fine)

xp = np.linspace(xmin, xmax, N_bins+1)
fp = f(xp)

# integral range
a = 0.5
b = 1.5
c = 2.5

#---------------------------------------------------------------------
# rectangle method
#---------------------------------------------------------------------
plt.plot(x, f(x), "r", linewidth=2)
plt.ylim(ymin = 0)

ax = plt.gca()

# shade region
x1 = a
x2 = b
fl = f(x1)

verts = [(x1, 0), (x1, fl), (x2, fl), (x2, 0)]
ax.add_patch(Polygon(verts, facecolor="0.8"))


fmax = fp.max()

for xl in xp:
    plt.plot([xl,xl], [0.0, 1.2*fmax], ls="--", color="0.5")

plt.scatter(xp, fp, marker="o", color="r", zorder=100)

plt.figtext(0.9, 0.05, '$x$', fontsize=20)
plt.figtext(0.1, 0.9, '$y$', fontsize=20)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((a, b))
ax.set_xticklabels(('$a$', '$b$'))
ax.set_yticks([])

plt.xlim(xmin, 1.05*xmax)

plt.savefig("rectangle.png", bbox_inches="tight")


#---------------------------------------------------------------------
# trapezoid method
#---------------------------------------------------------------------
plt.clf()

plt.plot(x, f(x), "r", linewidth=2)
plt.ylim(ymin = 0)

ax = plt.gca()

x1 = a
x2 = b

# shade region
f1 = f(x1)
f2 = f(x2)

verts = [(x1, 0), (x1, f1), (x2, f2), (x2, 0)]
ax.add_patch(Polygon(verts, facecolor="0.8"))

fmax = fp.max()

for xl in xp:
    plt.plot([xl,xl], [0.0, 1.2*fmax], ls="--", color="0.5")


ax.add_patch(Polygon(verts, facecolor="0.8"))

plt.scatter(xp, fp, marker="o", color="r", zorder=100)

plt.figtext(0.9, 0.05, '$x$', fontsize=20)
plt.figtext(0.1, 0.9, '$y$', fontsize=20)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((a, b))
ax.set_xticklabels(('$a$', '$b$'))
ax.set_yticks([])

plt.xlim(xmin, 1.05*xmax)

plt.savefig("trapezoid.png", bbox_inches="tight")


#---------------------------------------------------------------------
# simpsons method
#---------------------------------------------------------------------
plt.clf()

plt.plot(x, f(x), "r", linewidth=2)
plt.ylim(ymin = 0)

ax = plt.gca()


# shade region -- get the coefficients of the parabola
f0 = f(a)
f1 = f(b)
f2 = f(c)

delta = 0.5*(c-a)

A = (f0 - 2*f1 + f2)/(2*delta**2)
B = -(f2 - 4*f1 + 3*f0)/(2*delta)
C = f0

x1 = a
x2 = c
xsimp = np.linspace(x1,x2,100)
fsimp = A*(xsimp-x1)**2  + B*(xsimp-x1) + C

simpvert = list(zip(xsimp, fsimp))

verts = [(x1, 0)] + simpvert + [(x2, 0)]
ax.add_patch(Polygon(verts, facecolor="0.8"))

fmax = fp.max()

for xl in xp:
    plt.plot([xl,xl], [0.0, 1.2*fmax], ls="--", color="0.5")

plt.scatter(xp, fp, marker="o", color="r", zorder=100)

plt.figtext(0.9, 0.05, '$x$', fontsize=20)
plt.figtext(0.1, 0.9, '$y$', fontsize=20)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((a, b, c))
ax.set_xticklabels(('$a$', '$b$', '$c$'))
ax.set_yticks([])

plt.xlim(xmin, 1.05*xmax)

plt.savefig("simpsons.png",bbox_inches="tight")
