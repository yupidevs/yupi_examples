from yupi import Trajectory
from yupi.analyzing import plot_trajectories

# Data you got elsewhere
x = [0, 1.0, 0.63, -0.37, -1.24, -1.5, -1.08, -0.19, 0.82, 1.63, 1.99, 1.85]
y = [0, 0, 0.98, 1.24, 0.69, -0.3, -1.23, -1.72, -1.63, -1.01, -0.06, 0.94]

# Generate the trajectory object
track = Trajectory(x=x, y=y, traj_id="Spiral")

# Plot the results
plot_trajectories([track])