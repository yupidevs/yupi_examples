# yupi Examples

This repository contains a selection of examples to illustrate the usage of python library [yupi](https://github.com/yupidevs/yupi). Code examples are provided also with videos (in the cases where those are required) and camera calibration files.

Further description of yupi's API can be found in the [official documentation](https://yupi.readthedocs.io/en/latest/).

## Usage

After installing Yupi via the pypi package:

```
pip install yupi
```

Clone this repository:

```
git clone https://github.com/yupidevs/yupi_examples
```

And you should be able to run any of the provided examples like:

```
python example_XXX.py
```

## Description of current examples

Examples are divided into two different categories: intro and example. The first is designed to cover the very basics of yupi, while the later is designed to illustrate a more complex integration of yupi tools in order to reproduce the results of an existing (or yet to come) scientific paper. 

In this table you can easily find the examples that better suits you.

| Filename        | Related API functions                                                   | Description                                                         |
| --------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------- |
| intro_001.py    | yupi.Trajectory <br> yupi.analyzing.plot_trajectories                   | Creates a Trajectory using arrays of x and y, then plot it          | 
| intro_002.py    | yupi.analyzing.plot_trajectories <br> yupi.generating.RandomWalkGenerator | Generates a list of Trajectory objects and plot them all            |
| intro_003.py    | yupi.tracking.ROI<br> yupi.tracking.ObjectTracker<br> yupi.tracking.TrackingScenario<br> yupi.tracking.ColorMatching <br> yupi.analyzing.plot_trajectories | Extracts the trajectory of a blue ball inside a video of multiple balls and plots it |
| example_001.py  |  yupi.generating.LangevinGenerator <br> yupi.analyzing.plot_trajectories <br> yupi.analyzing.estimate_velocity_samples <br> yupi.analyzing.plot_velocity_hist <br> yupi.analyzing.estimate_turning_angles <br> yupi.analyzing.plot_angle_distribution <br> yupi.analyzing.estimate_msd  <br> yupi.analyzing.plot_msd  <br> yupi.analyzing.estimate_kurtosis <br> yupi.analyzing.plot_kurtosis <br> yupi.analyzing.estimate_vacf <br> yupi.analyzing.plot_vacf |  A simulation of the statistical properties for the motion of a lysozyme molecule in water. Several molecule trajectories are generated and later analyzed.   |
| example_002.py  |  yupi.analyzing.plot_trajectories <br> yupi.tracking.ROI <br> yupi.tracking.ObjectTracker <br> yupi.tracking.TrackingScenario <br> yupi.tracking.ColorMatching <br> yupi.tracking.FrameDifferencing <br> yupi.tracking.BackgroundEstimator  <br> yupi.tracking.BackgroundSubtraction  <br> yupi.tracking.TemplateMatching <br> yupi.tracking.OpticalFlow  |  A comparison of different tracking methods over the same input video where the camera is fixed at a constant distance from the plane where an ant moves.  |
| example_003.py  |  yupi.analyzing.plot_trajectories <br> yupi.tracking.ROI <br> yupi.tracking.ObjectTracker <br> yupi.tracking.TrackingScenario <br> yupi.tracking.ColorMatching  <br> yupi.tracking.TemplateMatching <br> yupi.Trajectory (operations on Trajectory objects) |  Tracking a scaled-size rover wheel moving over sand. The position is subsequently compared to the ideal position assuming it does not slip or sink.  |
| example_004.py  |  yupi.analyzing.plot_trajectories <br> yupi.tracking.ROI <br> yupi.tracking.ObjectTracker <br> yupi.tracking.TrackingScenario <br> yupi.tracking.ColorMatching  <br> yupi.tracking.RemapUndistorter  |  Tracking an intruder while penetrating a granular material in a quasi 2D enviroment.  |
| example_005.py  |  yupi.analyzing.plot_trajectories <br> yupi.tracking.ROI <br> yupi.tracking.CameraTracker <br> yupi.tracking.ObjectTracker <br> yupi.tracking.TrackingScenario <br> yupi.tracking.ColorMatching  <br> yupi.tracking.RemapUndistorter  |  Simultaneous tracking of an ant and the camera capturing its movement with the reconstruction of the trajectory of the ant respect its initial position.  |