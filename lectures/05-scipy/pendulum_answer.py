from scipy.integrate import ode
import numpy as np
import matplotlib.pyplot as plt

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


def int_pendulum(theta0, q, omega_d, b, tend):
    r = ode(rhs)
    r.set_integrator("dopri5", nsteps=150000)

    sol = []
    r.set_solout(lambda t, y: sol.append([t, *y]))

    t0 = 0.0
    omega0 = 0.0
    r.set_initial_value((theta0, omega0), t0)

    r.set_f_params(q, omega_d, b)

    r.integrate(tend)
    return np.array(sol)


s = int_pendulum(np.radians(60), 0.5, 0.6666, 1.5, 200.0)
q = int_pendulum(np.radians(60.001), 0.5, 0.6666, 1.5, 200.0)

plt.plot(s[:,0], restrict_theta(s[:,1]))
plt.plot(q[:,0], restrict_theta(q[:,1]))

plt.show()
