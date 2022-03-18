"""
Example 3:

Tracking a scaled-size rover wheel moving over sand.
The wheel is forced to move at a fixed angular velocity.
The actual linear velocity is subsequently computed
to evaluate how much does it differs from the ideal
velocity (a straight line assuming it does not slip
or sink).

The authors of [1] studied the motion of vehicles over
granular materials experimentally. In their work, they
report the analysis of the trajectories performed by a
scaled-size wheel while rolling over sand at two different
gravitational accelerations, exploiting the instrument
designed in [2]. This example aims to partially reproduce
some of the results shown in the paper using one of the
original videos provided by the authors.

In the video, one can observe a wheel which is forced to
move over sand at a fixed angular velocity. In optimal
rolling conditions, one can expect the wheel to move at a
constant linear velocity. However, due to slippery and
shrinkage, the actual linear velocity differs from the
one expected under ideal conditions. To study the factors
that affect the wheel motion, the first step is quantifying
how different is the rolling process respect to the expected
in ideal conditions.

This example addresses the problem of capturing the trajectory
of the wheel and computing its linear velocity, and the
efficiency of the rolling process.

A detailed explanation of this code can be found in:
https://yupi.readthedocs.io/en/latest/examples/example3.html


References
----------
[1] Amigó-Vega, J., et al. "Measuring the Performance of a Rover Wheel
In Martian Gravity." Revista Cubana de Física 36.1 (2019): 46-50.
[2] Viera-López, G., et al. "Note: Planetary gravities made simple:
Sample test of a Mars rover wheel." Review of Scientific Instruments
88.8 (2017): 086107.
"""

# Import dependencies
import cv2
from yupi.tracking import ROI, ObjectTracker, TrackingScenario
from yupi.tracking import ColorMatching, TemplateMatching
from yupi.graphics import plot_2D

# Specify path to the required resources
video_path = 'resources/videos/Viera2017.mp4'
template_path = 'resources/templates/pivot.png'

# Initialize main tracking objects
trackers = []

# Initialize TemplateMatching tracker for the central pivot
template = cv2.imread(template_path)
algorithm = TemplateMatching(template, threshold=0.5)
trackers.append( ObjectTracker('Central Pivot', algorithm, ROI((80, 80))) )

# Initialize ColorMatching tracker for the green led in the wheel
algorithm = ColorMatching((80,170,90), (190,255,190))
trackers.append( ObjectTracker('Green LED', algorithm, ROI((50, 50))) )

# Create a Tracking Scenario
scenario = TrackingScenario(trackers)

# Track the video using the preconfigured scenario
retval, tl = scenario.track(video_path, pix_per_m=4441, start_frame=160, end_frame=210)

# Computing the trajectory of the led referred to the center pivot
center, led = tl
led_centered = led - center
led_centered.traj_id = 'led'

# Computing the trajectory of the wheel referred to the center pivot
wheel_centered = led_centered.copy()
wheel_centered.add_polar_offset(0.039, 0)
wheel_centered.traj_id = 'wheel'
plot_2D([wheel_centered, led_centered])

# Computing the trajectory of the wheel referred to its initial position
wheel = wheel_centered - wheel_centered.r[0]

# Computing the linear velocity in optimal conditions (omega x r)
v_opt = 4 * 0.07

# Computing the linear velocity by the results of the tracking
v_meas = wheel.v.norm

#Computing the efficiency
eff = v_meas/v_opt

# Plotting the linear displacement of the wheel
import matplotlib.pyplot as plt
plt.plot(wheel.t, eff)
plt.xlabel('time [s]')
plt.ylabel('efficiency')
plt.show()
