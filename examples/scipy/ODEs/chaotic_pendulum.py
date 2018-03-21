"""Solve the chaotic damped driven pendulum using the newer SciPy IVP
ODE interfaces.  Passing optional arguments is now done using the
functools partial.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from functools import partial


def rhs(t, Y, q, omega_d, b):
    """ damped driven pendulum system derivatives.  Here, Y = (theta, omega) are
    the solution variables. """
    f = np.zeros_like(Y)

    f[0] = Y[1]
    f[1] = -q*Y[1] - np.sin(Y[0]) + b*np.cos(omega_d*t)

    return f

def restrict_theta(theta):
    """ convert theta to be restricted to lie between -pi and pi"""
    tnew = theta + np.pi
    tnew += -2.0*np.pi*np.floor(tnew/(2.0*np.pi))
    tnew -= np.pi
    return tnew

def integrate(Y0, tmax, q, omega_d, b, dt=0.05):

    r = solve_ivp(partial(rhs, q=q, omega_d=omega_d, b=b),
                  (0.0, tmax),
                  Y0,
                  dense_output=True)

    t = np.arange(0.0, tmax, dt)
    return t, r.sol(t)


if __name__ == "__main__":
    q = 0.5
    omega_d = 2./3.
    b = 1.5

    T_d = 2.0*np.pi/omega_d

    t, Y = integrate([np.radians(60), 0.0], 50*T_d, q, omega_d, b, dt=T_d/200.0)

    plt.plot(t, restrict_theta(Y[0,:]))
    plt.savefig("damped_pendulum.png")
