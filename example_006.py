"""
Example 6

A model framework of a diffusion process with fluctuating diffusivity
is presented. A Brownian but non-Gaussian diffusion by means of a coupled
set of stochastic differential equations is predicted. Position is
described by an overdamped Langevin equation and the diffusion coefficient
as the square of an Ornstein-Uhlenbeck process.

The example is focused in computing the probability density function for
displacements at different time instants for the case of a one-dimensional
process, as shown analitically by Chechkin et al. in [1] and discussed in [2].


References
----------
[1] Chechkin, Aleksei V., et al. "Brownian yet non-Gaussian diffusion:
from superstatistics to subordination of diffusing diffusivities."
Physical Review X 7.2 (2017): 021002.

[2] Thapa, Samudrajit, et al. "Bayesian analysis of single-particle
tracking data using the nested-sampling algorithm: maximum-likelihood
model selection applied to stochastic-diffusivity data." Physical
Chemistry Chemical Physics 20.46 (2018): 29018-29037.
"""

# Import dependencies
import numpy as np
from yupi.stats import collect_at_time
from yupi.graphics import plot_hists
from yupi.generators import DiffDiffGenerator

np.random.seed(0)

# Simulation parameters
T = 1000   # Total time of the simulation
N = 5000   # Number of trajectories
dt = .1    # Time step

# Simulating the process
dd = DiffDiffGenerator(T, N=N, dt=dt)
trajs = dd.generate()

# Setting different time instants
time_instants = np.array([1.0, 10.0, 100.0])

# Getting positions at different time instants
r = [collect_at_time(trajs, time=t, func=lambda r: r.x) for t in time_instants]

# Plotting
plot_hists(r, bins=30, density=True,
    labels=[f't = {t}' for t in time_instants],
    xlabel='x',
    ylabel='PDF',
    legend=True,
    grid=True,
    yscale='log',
    ylim=(1e-3, 1),
    xlim=(-20, 20),
    filled=True
)
