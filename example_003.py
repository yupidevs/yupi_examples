import cv2
from yupi.tracking import ROI, ObjectTracker, TrackingScenario
from yupi.tracking import ColorMatching, TemplateMatching
from yupi.analyzing import plot_trajectories

video_path = 'resources/videos/Viera2017.mp4'
template_path = 'resources/templates/pivot.png'

# Initialize main tracking objects
trackers = []

# # Initialize TemplateMatching tracker for the central pivot
template = cv2.imread(template_path)
algorithm = TemplateMatching(template, threshold=0.5)
trackers.append( ObjectTracker('center', algorithm, ROI((80, 80))) )

# Initialize ColorMatching tracker for the green led in the wheel
algorithm = ColorMatching((80,170,90), (190,255,190))
trackers.append( ObjectTracker('green led', algorithm, ROI((50, 50))) )

# Create a Tracking Scenario
scenario = TrackingScenario(trackers)

# Track the video using the preconfigured scenario
retval, tl = scenario.track(video_path, pix_per_m=4441, start_in_frame=154, end_in_frame=200)

# Computing the trajectory of the led referred to the center pivot
center, led = tl
led_centered = led - center
led_centered.id = 'led'

# Computing the trajectory of the wheel referred to the center pivot
wheel_centered = led_centered.copy()
wheel_centered.add_polar_offset(0.039, 0)
wheel_centered.id = 'wheel'
plot_trajectories([wheel_centered, led_centered])

# Computing the trajectory of the wheel referred to its initial position
wheel = wheel_centered - wheel_centered.r[0]

# Plotting the linear displacement of the wheel
import matplotlib.pyplot as plt
plt.plot(wheel.t, wheel.r.norm)
plt.xlabel('time [s]')
plt.ylabel('linear displacement [m]')
plt.show()
