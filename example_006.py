"""
Example 2:

A comparison of different tracking methods over the same input video
where the camera is fixed at a constant distance from the plane
where an ant moves.

In the work of Frayle-Pérez et. al [1], the authors studied the
capabilities of different image processing algorithms that can be
used for image segmentation and tracking of the motion of insects
under controlled environments. In this example, we are going to
illustrate a comparison of a subset of these algorithms and evaluate
them using one of the videos from the original paper.

A detailed explanation of this code can be found in:
https://yupi.readthedocs.io/en/latest/examples/example2.html


References
----------
[1] Frayle-Pérez, S., et al. "Chasing insects: a survey of tracking algorithms."
Revista Cubana de Fisica 34.1 (2017): 44-47.

"""
# Import dependencies
import cv2
from yupi.graphics import plot_2D
from yupi.tracking import (ROI, BackgroundEstimator, BackgroundSubtraction,
                           ColorMatching, FrameDifferencing, ObjectTracker,
                           OpticalFlow, TemplateMatching, TrackingScenario)

# Specify path to the required resources
video_path = "resources/videos/Frayle2017.mp4"
template_file = "resources/templates/ant_small.png"

# Initialize main tracking objects
trackers = []

# Initialize ColorMatching tracker
algorithm = ColorMatching((0, 0, 0), (150, 150, 150))
trackers.append(ObjectTracker("Ant (ColorMatching)", algorithm, ROI((50, 50), scale=0.5)))

# Initialize FrameDifferencing tracker
algorithm = FrameDifferencing(frame_diff_threshold=5)
trackers.append(ObjectTracker("Ant (FrameDifferencing)", algorithm, ROI((50, 50), scale=0.5)))

# Initialize BackgroundSubtraction tracker
background = BackgroundEstimator.from_video(video_path, 20)
algorithm = BackgroundSubtraction(background, background_threshold=5)
trackers.append(ObjectTracker("Ant (BackgroundSubtraction)", algorithm, ROI((50, 50), scale=0.5)))

# Initialize TemplateMatching tracker
template = cv2.imread(template_file)
algorithm = TemplateMatching(template, threshold=0.7)
trackers.append(ObjectTracker("Ant (TemplateMatching)", algorithm, ROI((50, 50), scale=0.5)))

# Initialize OpticalFlow tracker
algorithm = OpticalFlow(threshold=0.3, buffer_size=3)
trackers.append(ObjectTracker("Ant (OpticalFlow)", algorithm, ROI((50, 50), scale=0.5)))

# Create a Tracking Scenario
scenario = TrackingScenario(trackers, preview_scale=0.5)

# Track the video using the preconfigured scenario
retval, tl = scenario.track(video_path, pix_per_m=1024)
plot_2D(tl)
