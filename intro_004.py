import numpy as np
import yupi.graphics
import yupi.stats
from yupi.generators import LangevinGenerator

T = 500  # Total time (number of time steps if dt==1)
dim = 2  # Dimension of the walker trajectories
N = 500  # Number of random walkers
dt = 0.5  # Time step

tau = 2  # Relaxation time
sigma = 0.1  # Scale of the noise pdf


lg = LangevinGenerator(T, dim, N, dt, tau, sigma, seed=0)
trajs = lg.generate()


# Spacial trajectories
yupi.graphics.plot_2D(trajs[:10], legend=False)

# Velocity histogram
v = yupi.stats.speed_ensemble(trajs, step=1)
yupi.graphics.plot_velocity_hist(v, bins=20)

# Turning angles
theta = yupi.stats.turning_angles_ensemble(trajs)
yupi.graphics.plot_angles_hist(theta, 30)

# Mean square displacement
msd, msd_std = yupi.stats.msd(trajs, time_avg=True, lag=30)
yupi.graphics.plot_msd(msd, msd_std, dt, lag=30)

# Kurtosis
ref = yupi.stats.kurtosis_reference(trajs)
kurtosis, _ = yupi.stats.kurtosis(trajs, time_avg=False, lag=30)
yupi.graphics.plot_kurtosis(kurtosis, kurtosis_ref=ref, dt=dt)

# Velocity autocorrelation function
vacf, _ = yupi.stats.vacf(trajs, time_avg=True, lag=50)
yupi.graphics.plot_vacf(vacf, dt, 50)

# Power spectral density
psd_mean, psd_std, frec = yupi.stats.psd(trajs, lag=150)
yupi.graphics.plot_psd(psd_mean, frec, psd_std)
