import cv2
from yupi.tracking import ROI, ObjectTracker, TrackingScenario
from yupi.tracking import ColorMatching, FrameDifferencing
from yupi.tracking import BackgroundEstimator, BackgroundSubtraction
from yupi.tracking import TemplateMatching, OpticalFlow
from yupi.analyzing import plot_trajectories

video_path = 'resources/videos/Frayle2017.mp4'
template_file = 'resources/templates/ant_small.png'

# Initialize main tracking objects
trackers = []

# Initialize ColorMatching tracker
algorithm = ColorMatching((0,0,0), (150,150,150))
trackers.append( ObjectTracker('color_matching', algorithm, ROI((50, 50))) )

# Initialize FrameDifferencing tracker
algorithm = FrameDifferencing(frame_diff_threshold=5)
trackers.append( ObjectTracker('frame_diff', algorithm, ROI((50, 50))) )

# Initialize BackgroundSubtraction tracker
background = BackgroundEstimator.from_video(video_path, 20, 120)
algorithm = BackgroundSubtraction(background, background_threshold=5)
trackers.append( ObjectTracker('bkgnd_sub', algorithm, ROI((50, 50))) )

# Initialize TemplateMatching tracker
template = cv2.imread(template_file)
algorithm = TemplateMatching(template, threshold=0.7)
trackers.append( ObjectTracker('temp_match', algorithm, ROI((50, 50))) )

# Initialize FrameDifferencing tracker
algorithm = OpticalFlow(threshold=0.3, buffer_size=3)
trackers.append( ObjectTracker('optical_flow', algorithm, ROI((50, 50))) )


# Create a Tracking Scenario
scenario = TrackingScenario(trackers)

# Track the video using the preconfigured scenario
retval, tl = scenario.track(video_path, pix_per_m=1024, start_in_frame=120)
plot_trajectories(tl)