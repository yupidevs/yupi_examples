from yupi.tracking.trackers import ROI, ObjectTracker, TrackingScenario
from yupi.tracking.undistorters import RemapUndistorter
from yupi.tracking.algorithms import ColorMatching
from yupi.analyzing.visualization import plot_trajectories
from yupi import Trajectory

video_path = 'resources/videos/Diaz2020.MP4'
camera_file = 'resources/cameras/gph3+.npz'

# Initialize image undistorter
undistorter = RemapUndistorter(camera_file)

# Initialize tracker for the cyan dot
algorithm1 = ColorMatching((70,40,20), (160,80,20)) # BGR
cyan = ObjectTracker('cyan marker', algorithm1, ROI((50, 50)))

# Initialize tracker for the magenta dot
algorithm2 = ColorMatching((30,20, 50), (95, 45,120))         
magenta = ObjectTracker('magenta marker', algorithm2,  ROI((30, 50)))


# Initialize the Tracking scenario with the video
scenario = TrackingScenario([cyan, magenta], 
                            undistorter=undistorter)

# Track the video using the preconfigured scenario
retval, tl = scenario.track(video_path, pix_per_m=2826, start_in_frame=200)
plot_trajectories(tl)

Trajectory.save_trajectories(tl)