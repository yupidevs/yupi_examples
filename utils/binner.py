from typing import List, Union
import numpy as np


# Binner ------------->
# x  ----------------->
# y ------------------>
# edges -------------->
# count -------------->
# center_bins -------->
# y_binned -----------> binned
# y_binned_mean ------>
# y_binned_std ------->
# y_binned_sem ------->
# y_centered --------->
# y_stand ------------>
# y_binned_centered -->
# y_binned_stand ----->




class Binner:
    def __init__(
        self, x, y, count: int = 10, edges: Union[np.ndarray, None] = None
    ):
        self.y = y

        self.edges = edges if edges is not None else np.linspace(np.min(x), np.max(x), count + 1)
        self.count = len(self.edges) - 1                           # number of bins
        self.center_bins = (self.edges[:-1] + self.edges[1:]) / 2  # center of every bin
        
        self.y_binned: List[np.ndarray]  # gather elements in every bin
        
        self._y_binned_mean: Union[np.ndarray, None] = None # mean [len(mean) = len(group) = self.count]
        self._y_binned_std: Union[np.ndarray, None] = None  # standard deviation
        self._y_binned_sem: Union[np.ndarray, None] = None  # standard error of the mean

        self._y_centered: Union[np.ndarray, None] = None               # every element of `y` subtracted by its group mean
        self._y_stand: Union[np.ndarray, None] = None                  # every element of `y` standardized
        self._y_binned_centered: Union[List[np.ndarray], None] = None  # centered group (i.e., zero mean: mu=0)
        self._y_binned_stand: Union[List[np.ndarray], None] = None     # centered group (i.e., zero mean: mu=0)

        self.idx = self._digitize(x)
        self._populate()


    @property
    def y_binned_mean(self):
        if self._y_binned_mean is None:
            self._y_binned_mean = np.array(list(map(np.mean, self.y_binned)))
        return self._y_binned_mean

    @property
    def y_binned_std(self):
        if self._y_binned_std is None:
            self._y_binned_std = np.array(list(map(np.std, self.y_binned)))
        return self._y_binned_std

    @property
    def y_binned_sem(self):
        if self._y_binned_sem is None:
            std = self.y_binned_std
            sizes = [np.sqrt(yb.size) for yb in self.y_binned]
            self._y_binned_sem = std / sizes
        return self._y_binned_sem

    @property
    def y_binned_centered(self):
        if self._y_binned_centered is None:
            mean = self.y_binned_mean
            self._y_binned_centered = np.array([yb - mean[i] for i, yb in enumerate(self.y_binned)])
        return self._y_binned_centered

    @property
    def y_binned_stand(self):
        if self._y_binned_stand is None:
           std = np.where(self.y_binned_std != 0, self.y_binned_std, np.nan)
           self._y_binned_stand = self.y_binned_centered / std
        return self._y_binned_stand

    @property
    def y_centered(self):
        if self._y_centered is None:
            y_mean = self.y_binned_mean[self.idx - 1]
            self._y_centered = self.y - y_mean
        return self._y_centered

    @property
    def y_stand(self):
        if self._y_stand is None:
            y_std = self.y_binned_std[self.idx - 1]
            with np.errstate(divide='ignore', invalid='ignore'):
                self._y_stand = np.where(y_std == 0, np.nan, self.y_centered / y_std)
        return self._y_stand

    def _digitize(self, x):
        idx = np.digitize(x, self.edges)
        idx[idx == self.count + 1] -= 1   # close last interval bin
        return idx

    def _populate(self):
        self.y_binned = [np.array([np.nan]) for _ in range(self.count)]
        for idx_ in np.unique(self.idx):
            mask = self.idx == idx_
            self.y_binned[idx_ - 1] = self.y[mask]
