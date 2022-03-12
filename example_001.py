"""
Example 1:

A simulation of the statistical properties for the motion of
a lysozyme molecule in water is presented using `yupi` API.
The simulation shows cualitatively the classical scaling laws of
the Langevin theory to explain Brownian Motion (those for Mean
Square Displacement or Velocity Autocorrelation Function).


References
----------
# [1] Berg, Howard C. Random walks in biology. Princeton University Press, 1993.
# [2] Colvin, J. Ross. "The size and shape of lysozyme." Canadian Journal of Chemistry 30.11 (1952): 831-834.
"""

import numpy as np
import matplotlib.pyplot as plt
from yupi.generators import LangevinGenerator
from yupi.stats import (
    msd,
    speed_ensemble,
    vacf,
    turning_angles_ensemble,
    kurtosis,
    kurtosis_reference
)
from yupi.graphics import (
    plot_2D,
    plot_angles_hist,
    plot_kurtosis,
    plot_msd,
    plot_vacf,
    plot_velocity_hist
)

## 1. Simulation and model parameters

# Physical constants and system properties
N0 = 6.02e23     # Avogadro's constant [1/mol]
k = 1.38e-23     # Boltzmann's constant [J/mol.K]
T = 300          # absolute temperature [K]
eta = 1.002e-3   # water viscosity [Pa.s]
M = 14.1         # lysozyme molar mass [kg/mol] [1]
d1 = 90e-10      # semi-major axis [m] [2]
d2 = 18e-10      # semi-minor axis [m] [2]

# Auxiliary model parameters
m = M / N0                    # mass of one molecule
a = np.sqrt(d1/2 * d2/2)      # radius of the molecule
alpha = 6 * np.pi * eta * a   # Stoke's coefficient
v_eq = np.sqrt(k * T / m)     # equilibrium thermal velocity

# Model/generator parameters
tau = (alpha / m)**-1                   # relaxation time
sigma = np.sqrt(2 / tau) * v_eq   # scale parameter of noise pdf

# Simulation parameters
dim = 2           # trajectory dimension
N = 1000          # number of trajectories
dt = 1e-1 * tau   # time step
tt = 50 * tau     # total time


## 2. Simulating the process

lg = LangevinGenerator(tt, dim, N, dt, tau, sigma, seed=0)
trajs = lg.generate()


## 3. Data analysis and plots

plt.figure(figsize=(9,5))

# Spacial trajectories
plt.subplot(231)
plot_2D(trajs[:5], legend=False, show=False)

#  velocity histogram
v_norm = speed_ensemble(trajs)
plt.subplot(232)
plot_velocity_hist(v_norm, bins=20, show=False)

#  turning angles
theta = turning_angles_ensemble(trajs)
plt.subplot(233, projection='polar')
plot_angles_hist(theta, bins=60, show=False)

#  velocity autocorrelation function
lag_vacf = 50
vacf, _ = vacf(trajs, time_avg=True, lag=lag_vacf)
plt.subplot(234)
plot_vacf(vacf, dt, lag_vacf, show=False)

#  mean square displacement
lag_msd = 30
msd, msd_std = msd(trajs, time_avg=True, lag=lag_msd)
plt.subplot(235)
plot_msd(msd, msd_std, dt, lag=lag_msd, show=False)

#  kurtosis
kurt, _ = kurtosis(trajs, time_avg=False)
kurt_ref = kurtosis_reference(trajs)
plt.subplot(236)
plot_kurtosis(kurt, dt=dt, kurtosis_ref=kurt_ref, show=False)


# Generate plot
plt.tight_layout()
plt.show()
