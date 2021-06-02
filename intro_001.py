from yupi import Trajectory
from yupi.analyzing.visualization import plot_trajectory

# Creation by assigning the axis directly

# Data you got elsewhere
x = [0, 1.0, 0.63, -0.37, -1.24, -1.5, -1.08, -0.19, 0.82, 1.63, 1.99, 1.85]
y = [0, 0, 0.98, 1.24, 0.69, -0.3, -1.23, -1.72, -1.63, -1.01, -0.06, 0.94]

# Generate the trajectory object
track = Trajectory(x=x, y=y, traj_id="Spiral")

# Plot the results
plot_trajectory(track, title='Assigning the axis directly')

# Creation by assigning the dimensions data

# Data you got elsewhere
dims = [
    [0, 1.0, 0.63, -0.37, -1.24, -1.5, -1.08, -0.19, 0.82, 1.63, 1.99, 1.85],
    [0, 0, 0.98, 1.24, 0.69, -0.3, -1.23, -1.72, -1.63, -1.01, -0.06, 0.94]
]

# Generate the trajectory object
track = Trajectory(dimensions=dims, traj_id="Spiral")

# Plot the results
plot_trajectory(track, title='Assigning the dimensions data')

# Creation by assigning the points data

# Data you got elsewhere
points = [[0, 0], [1.0, 0], [0.63, 0.98], [-0.37, 1.24], [-1.24, 0.69],
          [-1.5, -0.3], [-1.08, -1.23], [-0.19, -1.72], [0.82, -1.63],
          [1.63, -1.01], [1.99, -0.06], [1.85, 0.94]]

# Generate the trajectory object
track = Trajectory(points=points, traj_id="Spiral")

# Plot the results
plot_trajectory(track, title='Assigning the points data')
