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

import matplotlib.pyplot as plt
import numpy as np
from yupi.generators import LangevinGenerator
from yupi.graphics import plot_2d
from yupi.stats.kurtosis import KurtosisStat
from yupi.stats.msd import MsdTimeAvgStat
from yupi.stats.speed import SpeedStat
from yupi.stats.turning_angles import TurningAngleStat
from yupi.stats.vacf import VacfTimeAvgStat

## 1. Simulation and model parameters

# Physical constants and system properties
N0 = 6.02e23  # Avogadro's constant [1/mol]
k = 1.38e-23  # Boltzmann's constant [J/mol.K]
T = 300  # absolute temperature [K]
eta = 1.002e-3  # water viscosity [Pa.s]
M = 14.1  # lysozyme molar mass [kg/mol] [1]
d1 = 90e-10  # semi-major axis [m] [2]
d2 = 18e-10  # semi-minor axis [m] [2]

# Auxiliary model parameters
m = M / N0  # mass of one molecule
a = np.sqrt(d1 / 2 * d2 / 2)  # radius of the molecule
alpha = 6 * np.pi * eta * a  # Stoke's coefficient
v_eq = np.sqrt(k * T / m)  # equilibrium thermal velocity
tau = m / alpha  # relaxation time

# Model/generator parameters
gamma = 1 / tau  # drag parameter
sigma = np.sqrt(2 / tau) * v_eq  # scale parameter of noise pdf

# Simulation parameters
dim = 2  # trajectory dimension
N = 1000  # number of trajectories
dt = 1e-1 * tau  # time step
tt = 50 * tau  # total time


## 2. Simulating the process

lg = LangevinGenerator(T=tt, dim=dim, dt=dt, gamma=gamma, sigma=sigma, seed=0)
trajs = lg.generate(N)


## 3. Data analysis and plots

plt.figure(figsize=(9, 5))

# Spacial trajectories
plot_2d(trajs[:5], legend=False, ax=plt.subplot(231), show=False)

# Speed histogram
SpeedStat(trajs).plot(bins=20, ax=plt.subplot(232), show=False)

# Turning angles
TurningAngleStat(trajs).plot(
    bins=60, ax=plt.subplot(233, projection="polar"), show=False
)

# Velocity autocorrelation function
VacfTimeAvgStat(trajs, lag=50).plot(ax=plt.subplot(234), show=False)

# Mean square displacement
MsdTimeAvgStat(trajs, lag=50).plot(ax=plt.subplot(235), show=False)

# Kurtosis
KurtosisStat(trajs).plot(ax=plt.subplot(236), show=False)

# Generate plot
plt.tight_layout()
plt.show()
