from yupi.tracking import ROI, ObjectTracker, TrackingScenario
from yupi.tracking import ColorMatching
from yupi.graphics import plot_2D


# Initialize main tracking objects
algorithm = ColorMatching((180,125,35), (190,135,45))
blue_ball = ObjectTracker('blue', algorithm, ROI((100, 100)))
scenario = TrackingScenario([blue_ball])

# Track the video using the preconfigured scenario
retval, tl = scenario.track('resources/videos/demo.avi', pix_per_m=10)
plot_2D(tl)
