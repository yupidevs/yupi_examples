from yupi.tracking.trackers import ROI, ObjectTracker, CameraTracker, TrackingScenario
from yupi.tracking.undistorters import RemapUndistorter
from yupi.tracking.algorithms import ColorMatching
from yupi.analyzing.visualization import plot_trajectories


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
plot_trajectories(tl)