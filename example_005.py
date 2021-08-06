"""
Example 5:

Simultaneous tracking of an ant and the camera capturing its movement
with the reconstruction of the trajectory of the ant respect its
initial position.

The robot designed in [1] allowed to extend the study of the motion
of insects for longer times and wider regions. The robot, keeping
a proper distance from the insect, continuously moves to preserve
the insect always in the scene recorded by its camera.

However, the fact of having both, the insect and the camera, moving at
the same time, introduces additional complications while reconstructing
the trajectory from a video source. yupi handles the motion of the camera
naturally as part of the TrackingScenario.

In this example, we shown how to reproduce the results of the original paper,
using one of the videos the authors used to compute the position of an
ant respect its original position, dealing with the movement of the camera.

A detailed explanation of this code can be found in:
https://yupi.readthedocs.io/en/latest/examples/example5.html


References
----------
[1] Serrano-Muñoz, A., et al. "An autonomous robot for continuous tracking
of millimetric-sized walkers." Review of Scientific Instruments 90.1 (2019):
014102.

"""
# Import dependencies
from yupi.tracking import ROI, ObjectTracker, CameraTracker, TrackingScenario
from yupi.tracking import RemapUndistorter
from yupi.tracking import ColorMatching
from yupi.graphics import plot_2D

# Specify path to the required resources
video_path = 'resources/videos/Serrano2019.mp4'
camera_file = 'resources/cameras/gph3+1080-60fps-MEDIUM.npz'


# Initialize main tracking objects
algorithm = ColorMatching((20,20,20), (65,65,65))
ant = ObjectTracker('ant', algorithm, ROI((120, 120), scale=0.75))
camera = CameraTracker(ROI((.65, .65), ROI.CENTER_INIT_MODE))
undistorter = RemapUndistorter(camera_file)
scenario = TrackingScenario([ant], camera, undistorter, preview_scale=0.75)

# Track the video using the preconfigured scenario
retval, tl = scenario.track(video_path, pix_per_m=6300)
plot_2D(tl)
