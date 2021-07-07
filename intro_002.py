from yupi.analyzing import plot_trajectories
from yupi.generating import RandomWalkGenerator

# Set parameter values
T = 500     # Total time (number of time steps if dt==1)
dim = 2     # Dimension of the walker trajectories
N = 3       # Number of random walkers
dt = 1      # Time step

# Probability of every action to be taken
# according to every axis (the actions are [-1, 0, 1])
prob = [[.5, .1, .4],   # x-axis
        [.5,  0, .5]]   # y-axis

# Get RandomWalk object and get position vectors
rw = RandomWalkGenerator(T, dim, N, dt, prob)
tr = rw.generate()
plot_trajectories(tr)
