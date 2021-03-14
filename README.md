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

In this table you can easily find the examples that suit you more.

| Filename        | Related API functions                                                   | Description                                                         |
| --------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------- |
| intro_001.py    | yupi.Trajectory <br> yupi.analyzing.plot_trajectories                   | Creates a Trajectory using arrays of x and y, then plot it          | 
| intro_002.py    | yupi.analyzing.plot_trajectories <br> yupi.generating.LangevinGenerator | Generates a list of Trajectory objects and plot them all            |
| intro_003.py    | yupi.tracking.ROI<br> yupi.tracking.ObjectTracker<br> yupi.tracking.TrackingScenario<br> yupi.tracking.ColorMatching <br> yupi.analyzing.plot_trajectories | Extracts the trajectory of a blue ball inside a video of multiple balls and plots it |