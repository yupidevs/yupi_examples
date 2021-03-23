from yupi.analyzing import plot_trajectories
from yupi.generating import LatticeRandomWalkGenerator
    
# set parameter values
T = 500
dim = 2
N = 5
dt = 1
actions = [1, 0, -1]
prob = [[.5, .1, .4],
        [.5, 0, .5]]

# get RandomWalk object and get position vectors
rw = LatticeRandomWalkGenerator(T, dim, N, dt, actions, prob)
tr = rw.generate()
plot_trajectories(tr)
