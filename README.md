# **yupi** examples

This repository contains a selection of examples to illustrate the usage of the python library [yupi](https://github.com/yupidevs/yupi).  Code examples are provided also with videos (in the cases where those are required) and camera calibration files.

Further description of yupi's API can be found in the [official documentation](https://yupi.readthedocs.io/en/latest/).

## Getting started


### Installing required packages

To be able to execute the examples you first need to install **yupi**:

```shell
pip install yupi
```

Some of the examples are distributed as **jupyter** notebooks, so installing **jupyter** is also recommended:

```shell
pip install jupyter
```

### Copying the examples

To get a local copy of the code examples and all the multimedia resources required just run:

```shell
git clone https://github.com/yupidevs/yupi_examples
```

### Executing the examples

Depending on the example extension, you have to execute it using python directly or jupyter.

For the examples distributed as `.py` files, simply run:

```shell
python example_XXX.py
```

For the examples distributed as `.ipynb` files, run instead:

```shell
jupyter notebook intro_XXX.ipynb
```

> This will open a browser window with the notebook.

## Description of current examples

Examples are divided into two different categories: introductory tutorials and advanced examples. The first is designed to cover the very basics of **yupi**, while the later is designed to illustrate a more complex integration of **yupi** tools in order to reproduce the results of published research.

In this table you can easily find the examples that better suits you.

| Filename        | Related API functions                                                   | Description                                                         |
| --------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------- |
| intro_000.ipynb    | Almost every yupi function :)                                    | Showcases minimal examples of most of the yupi APIs in a jupyter notebook   |
| intro_001.ipynb    | yupi.Trajectory <br> yupi.graphics.plot_2D                              | Creates a Trajectory using arrays of x and y, then plot it          |
| intro_002.ipynb    | yupi.graphics.plot_2D <br> yupi.generators.RandomWalkGenerator          | Generates a list of Trajectory objects and plot them all            |
| intro_003.ipynb    | yupi.tracking.ROI<br> yupi.tracking.ObjectTracker<br> yupi.tracking.TrackingScenario<br> yupi.tracking.ColorMatching <br> yupi.graphics.plot_2D | Extracts the trajectory of a blue ball inside a video of multiple balls and plots it |
| intro_004.ipynb  |  yupi.generators.LangevinGenerator <br> yupi.graphics.plot_2D <br> yupi.stats.speed_ensemble <br> yupi.graphics.plot_speed_hist <br> yupi.stats.turning_angles_ensemble <br> yupi.graphics.plot_angles_hist <br> yupi.stats.msd  <br> yupi.graphics.plot_msd  <br> yupi.stats.kurtosis <br> yupi.graphics.plot_kurtosis <br> yupi.stats.vacf <br> yupi.graphics.plot_vacf <br> yupi.stats.psd <br> yupi.graphics.plot_psd  |  A general showcase of the stats and graphics modules.   |
| intro_005.ipynb    | yupi.Trajectory  <br> yupi.VelocityMethod  <br> yupi.WindowType    | Details the differences among the available methods in **yupi** to estimate velocity  |
| example_001.py  |  yupi.generators.LangevinGenerator <br> yupi.graphics.plot_2D <br> yupi.stats.speed_ensemble <br> yupi.graphics.plot_speed_hist <br> yupi.stats.turning_angles_ensemble <br> yupi.graphics.plot_angles_hist <br> yupi.stats.msd  <br> yupi.graphics.plot_msd  <br> yupi.stats.kurtosis <br> yupi.graphics.plot_kurtosis <br> yupi.stats.vacf <br> yupi.graphics.plot_vacf |  A simulation of the statistical properties for the motion of a lysozyme molecule in water. Several molecule trajectories are generated and later analyzed.   |
| example_002.py  |  yupi.generators.DiffDiffGenerator <br> yupi.stats.collect <br> yupi.graphics.plot_hists |  A model framework of a diffusion process with fluctuating diffusivity is presented.  |
| example_003.py  |  yupi.graphics.plot_2D <br> yupi.tracking.ROI <br> yupi.tracking.ObjectTracker <br> yupi.tracking.TrackingScenario <br> yupi.tracking.ColorMatching  <br> yupi.tracking.TemplateMatching <br> yupi.Trajectory (operations on Trajectory objects) |  Tracking a scaled-size rover wheel moving over sand. The position is subsequently compared to the ideal position assuming it does not slip or sink.  |
| example_004.py  |  yupi.graphics.plot_2D <br> yupi.tracking.ROI <br> yupi.tracking.ObjectTracker <br> yupi.tracking.TrackingScenario <br> yupi.tracking.ColorMatching  <br> yupi.tracking.RemapUndistorter  |  Tracking an intruder while penetrating a granular material in a quasi 2D enviroment.  |
| example_005.py  |  yupi.graphics.plot_2D <br> yupi.tracking.ROI <br> yupi.tracking.CameraTracker <br> yupi.tracking.ObjectTracker <br> yupi.tracking.TrackingScenario <br> yupi.tracking.ColorMatching  <br> yupi.tracking.RemapUndistorter  |  Simultaneous tracking of an ant and the camera capturing its movement with the reconstruction of the trajectory of the ant respect its initial position.  |
| example_006.py  |  yupi.graphics.plot_2D <br> yupi.tracking.ROI <br> yupi.tracking.ObjectTracker <br> yupi.tracking.TrackingScenario <br> yupi.tracking.ColorMatching <br> yupi.tracking.FrameDifferencing <br> yupi.tracking.BackgroundEstimator  <br> yupi.tracking.BackgroundSubtraction  <br> yupi.tracking.TemplateMatching <br> yupi.tracking.OpticalFlow  |  A comparison of different tracking methods over the same input video where the camera is fixed at a constant distance from the plane where an ant moves.  |
