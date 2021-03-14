import numpy as np
from yupi.analyzing import plot_trajectories
from yupi.generating import LangevinGenerator

# Define general Generator parameter values
N = 3           # Number of trajectories
dim = 2         # Number of dimensions
T = 5 * 60      # Total simulation time
dt = .05        # Time step

# Define model-specific Generator values
tau = 1.	
kTm = 10
scale = np.sqrt(2 * kTm / tau)
pdf_name = 'normal'
v0 = scale * np.random.randn(N)

# Create the Generator object
le = LangevinGenerator(T, dim, N, dt, tau, pdf_name, scale, v0=v0)

# Generate the trajectories
tr = le.generate()

# Plot the results
plot_trajectories(tr)
