import numpy as np
from scipy.integrate import ode
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

def int_pendulum(theta0, q, omega_d, b, tend, dt):
    """ integrate the pendulum with a fixed timestep, dt"""
    r = ode(rhs)
    r.set_integrator("dopri5", nsteps=150000, first_step=dt, max_step=dt, dfactor=1.0)

    sol = []
    r.set_solout(lambda t, y: sol.append([t, *y]))

    t0 = 0.0
    omega0 = 0.0
    r.set_initial_value((theta0, omega0), t0)

    r.set_f_params(q, omega_d, b)

    r.integrate(tend)
    return np.array(sol)

def power_spectrum(t, theta0):
    """ return the power spectrum of theta.  For the frequency
        component, return it in terms of omega """

    theta = restrict_theta(theta0)
    
    # fill in the rest -- take the FFT of theta and return omega_k and 
    # the transform of theta
    N = len(t)    
    F = (2.0/N)*np.fft.rfft(theta)

    k = np.fft.rfftfreq(N)
    kfreq = 2.0*np.pi*k*N/max(t)

    return kfreq, F


# normal (undamped, not driven pendulum)
s = int_pendulum(np.radians(10), 0.0, 0.6666, 0.0, 200.0, 0.1)

omega, F = power_spectrum(s[:,0], s[:,1])

plt.plot(omega, np.abs(F)**2)
plt.xlim(0.0, 2.0)
plt.show()

# chaotic pendulum
s = int_pendulum(np.radians(10), 0.5, 0.6666, 1.15, 200.0, 0.1)

omega, F = power_spectrum(s[:,0], s[:,1])

plt.plot(omega, np.abs(F)**2)
plt.xlim(0.0, 2.0)
plt.show()
