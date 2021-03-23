from yupi.analyzing import plot_trajectories
from yupi.generating import LatticeRandomWalkGenerator
    
# set parameter values
T = 500     # total time (number of time steps if dt==1)
dim = 2     # dimension of the walker trajectories
N = 3       # number of random walkers
dt = 1      # time step

# vector of actions the walker can take:
# [move to the right/up, stay quiet, move to the left/down]
actions = [1, 0, -1]

# probability of every action to be taken
# according to every axis
prob = [[.5, .1, .4],  # x-axis
        [.5, 0, .5]]   # y-axis

# get RandomWalk object and get position vectors
rw = LatticeRandomWalkGenerator(T, dim, N, dt, actions, prob)
tr = rw.generate()
plot_trajectories(tr)
