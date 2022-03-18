"""
Example 4:

Tracking an intruder while penetrating a granular
material in a quasi 2D enviroment.

The work carried out in [1] studied
penetration of an intruder inside a granular material,
focusing in the influence of a wall for the trajectory
of the intruder. The authors tested different configurations
and observed specific phenomenons during the penetration
process (i.e. repulsion and rotation), enabling the
quantification of those phenomenons and its dependence
with the initial distance of the intruder from the wall.

In this example, we provide a script that extracts the
trajectory of the intruder from one of the videos used
to produce the results of the original paper. Moreover,
we include details to generate a plot that looks like the
one presented in the paper.

A detailed explanation of this code can be found in:
https://yupi.readthedocs.io/en/latest/examples/example4.html


References
----------
[1] Díaz-Melián, V. L., et al. "Rolling away from the Wall
into Granular Matter." Physical Review Letters 125.7 (2020):
078002.

"""
# Import dependencies
from numpy import pi
from yupi.tracking.trackers import ROI, ObjectTracker, TrackingScenario
from yupi.tracking.undistorters import RemapUndistorter
from yupi.tracking.algorithms import ColorMatching
from yupi.graphics import plot_2D

# Specify path to the required resources
video_path = 'resources/videos/Diaz2020.MP4'
camera_file = 'resources/cameras/gph3+.npz'

# Initialize image undistorter
undistorter = RemapUndistorter(camera_file)

# Initialize tracker for the center dot
algorithm1 = ColorMatching((70,40,20), (160,80,20)) # BGR
cyan = ObjectTracker('center marker', algorithm1, ROI((50, 50)))

# Initialize tracker for the magenta dot
algorithm2 = ColorMatching((30,20, 50), (95, 45,120))        
magenta = ObjectTracker('border marker', algorithm2,  ROI((30, 50)))


# Initialize the Tracking scenario with the video
scenario = TrackingScenario([cyan, magenta],
                            undistorter=undistorter)

# Track the video using the preconfigured scenario
retval, tl = scenario.track(video_path, pix_per_m=2826, start_frame=200)
plot_2D(tl)


# Rotate trajectories to be consistent with gravity
tl[0].rotate2d(- pi / 2)
tl[1].rotate2d(- pi / 2)

# Center trajectories respect the center of the intruder
off = tl[0].r[0]
tl[1] -= off
tl[0] -= off

# Show a plot of the conected components of the tracking
plot_2D(tl, line_style='-o', connected=True)
