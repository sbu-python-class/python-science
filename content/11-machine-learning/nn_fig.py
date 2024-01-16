import random

import matplotlib.pyplot as plt
import numpy as np


class Neuron(object):
    def __init__(self, x, y, R=0.35):
        self.x = x
        self.y = y
        self.R = R

    def draw(self, color="C0", label=None):
        theta = np.linspace(0, 2*np.pi, 180)
        xc = self.x + self.R*np.cos(theta)
        yc = self.y + self.R*np.sin(theta)

        plt.fill(xc, yc, color=color, alpha=0.75)

        if label is not None:
            plt.text(self.x, self.y, label, color="k", 
                     horizontalalignment="center", verticalalignment="center")


class Layer(object):
    def __init__(self, x, num_neurons=3, dy=1.0):
        self.x = x
        self.dy = dy
        self.num_neurons = num_neurons
        self.neurons = []

        for i in range(self.num_neurons):
            y = -i*self.dy
            self.neurons.append(Neuron(self.x, y))

    def draw(self, color="C1", label=None, top_label=None):
        # compute the bounding box
        ys = [q.y for q in self.neurons]

        ymin = min(ys) - self.neurons[0].R
        ymax = max(ys) + self.neurons[0].R

        xmin = self.neurons[0].x - self.neurons[0].R
        xmax = self.neurons[0].x + self.neurons[0].R

        dx = xmax - xmin
        xmin -= 0.25*dx
        xmax += 0.25*dx
        ymin -= 0.25*dx
        ymax += 0.25*dx

        plt.fill([xmin, xmin, xmax, xmax, xmin],
                 [ymin, ymax, ymax, ymin, ymin], 
                 color=color, zorder=-100, alpha=0.5, edgecolor="none")

        for i, n in enumerate(self.neurons):
            n.draw(label="{}".format(i))

        if label is not None:
            plt.text(self.x, ymin-0.5*dx, label,
                     horizontalalignment="center", color="k")

        if top_label is not None:
            plt.text(self.x, ymax+0.25*dx, top_label,
                     horizontalalignment="center", color="k")

class NeuralNet(object):

    def __init__(self, dx=2.0, nlayers=2, neurons_in=3, neurons_out=2):
        self.nlayers = nlayers

        self.layers = []
        for i in range(self.nlayers):
            if i == 0:
                neurons = neurons_in
            elif i == nlayers-1:
                neurons = neurons_out
            else:
                neurons = int(1.5*neurons_in)

            self.layers.append(Layer(i*dx, num_neurons=neurons, dy=1.5))

    def draw(self):
        for i, l in enumerate(self.layers):
            if i == 0:
                label = "input\nlayer {}".format(i+1)
                top_label = r"${\bf x}$"
            elif i == len(self.layers)-1:
                label = "output\nlayer {}".format(i+1)
                if len(self.layers) == 3:
                    top_label = r"${\bf z} = g({\bf A}\tilde{\bf z})$"
                else:
                    top_label = r"${\bf z} = g({\bf A}{\bf x})$"
            else:
                label = "hidden\nlayer {}".format(i+1)
                top_label = r"$\tilde{\bf z} = g({\bf B x})$"

            l.draw(label=label, top_label=top_label)

        colors = ["0.5", "C1", "C2", "C3", "C4", "C5", "C6"]

        # now connect
        for i in range(0, len(self.layers)-1):
            for j, n in enumerate(self.layers[i].neurons):
                x0 = n.x
                y0 = n.y
                R0 = n.R

                c = random.choice(colors)

                for q in self.layers[i+1].neurons:
                    xt = q.x
                    yt = q.y
                    Rt = q.R

                    # figure out the angle
                    theta = np.arctan2(yt-y0, xt-x0)
                    L = np.sqrt((xt - x0)**2 + (yt - y0)**2) - Rt - R0

                    plt.arrow(x0+R0*np.cos(theta), y0+R0*np.sin(theta), 
                              L*np.cos(theta), L*np.sin(theta), 
                              head_width=0.075, zorder=-50, 
                              color=c,
                              length_includes_head=True)

            xc = 0.5*(self.layers[i].x + self.layers[i+1].x)
            yc = self.layers[i].neurons[0].y + 0.25*(self.layers[i].neurons[0].y - self.layers[i].neurons[1].y)
            if i == 0 and self.nlayers > 2:
                label = r"${\bf B}$"
            else:
                label = r"${\bf A}$"

            plt.text(xc, yc, label, color="r")

        # draw inputs and outputs
        ls = self.layers[0]
        xf = ls.neurons[0].x - 1.5*ls.neurons[0].R
        L = 2.0*ls.neurons[0].R

        for n in ls.neurons:
            plt.arrow(xf - L, n.y, L, 0, head_width=0.075, color="k")

        ls = self.layers[-1]
        xf = ls.neurons[0].x + 1.25*ls.neurons[0].R
        L = 2.0*ls.neurons[0].R

        for n in ls.neurons:
            plt.arrow(xf, n.y, L, 0, head_width=0.075, color="k")


# simple version
nn = NeuralNet()
nn.draw()

plt.axis("off")
ax = plt.gca()
ax.set_aspect("equal", "datalim")

f = plt.gcf()
f.set_size_inches(5, 5)

plt.tight_layout()
plt.savefig("nn_fig.png", dpi=150, bbox_inches="tight")

# hidden layer
plt.clf()

nn = NeuralNet(nlayers=3)
nn.draw()

plt.axis("off")
ax = plt.gca()
ax.set_aspect("equal", "datalim")

f = plt.gcf()
f.set_size_inches(7, 5.5)
plt.tight_layout()
plt.savefig("nn_fig_hidden.png", dpi=150)

# add some labels
