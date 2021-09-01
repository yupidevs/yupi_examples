"""
Example 6

A model framework of a diffusion process with fluctuating diffusivity 
is presented. A Brownian but non-Gaussian diffusion by means of a coupled 
set of stochastic differential equations is predicted. Position is 
described by an overdamped Langevin equation and the diffusion coefficient 
as the square of an Ornstein-Uhlenbeck process.

The example is focused in computing the probability density function for 
displacements at different time instants for the case of a one-dimensional 
process, as shown analitically by Chechkin et al. in [1].


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
import matplotlib.pyplot as plt
from yupi.generators import DiffDiffGenerator


np.random.seed(0)

# Simulation parameters
T = 1000   # Total time of the simulation
N = 5000   # Number of trajectories
dt = .1    # Time step

# Setting different time instants
delta_t = np.array([1, 10, 100])   # Time instants
steps = np.int32(delta_t / dt)     # Same but in steps of the simulation

# Simulating the process
dd = DiffDiffGenerator(T, N=N, dt=dt)
trajs = dd.generate()

# Getting positions at different time intervals
r = [[traj.r.x[step] for traj in trajs] for step in steps]

# Plotting
for r_, delta_t_ in zip(r, delta_t):
    plt.hist(r_, bins=30, density=True, histtype='step',
             label=f't = {delta_t_}')
plt.legend()
plt.grid(True)
plt.ylim(1e-3, 1)
plt.xlim(-20, 20)
plt.yscale('log')
plt.xlabel('x')
plt.ylabel('PDF')
plt.show()