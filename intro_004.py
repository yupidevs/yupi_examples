import numpy as np
import yupi.stats
import yupi.graphics
from yupi.transformations import exp_convolutional_filter
from yupi.generators import LangevinGenerator


np.random.seed(0)

T = 500     # Total time (number of time steps if dt==1)
dim = 2     # Dimension of the walker trajectories
N = 500       # Number of random walkers
dt = 0.5    # Time step

tau = 2               # Relaxation time
noise_pdf = 'normal'  # Noise probabilistic distribution function
noise_scale = 0.1     # Scale of the noise pdf


lg = LangevinGenerator(T, dim, N, dt, tau, noise_pdf, noise_scale)
trajs = lg.generate()
traj = trajs[0]


# Spacial trajectories
yupi.graphics.plot_2D(trajs[:10], legend=False)

# Filter
traj.traj_id = 'non filtered'
smoothed_traj = exp_convolutional_filter(traj, 1, 'filtered')
yupi.graphics.plot_2D([traj, smoothed_traj], legend=True)

# Velocity histogram
v = yupi.stats.speed_ensemble(trajs, step=1)
yupi.graphics.plot_velocity_hist(v, bins=20)

# Turning angles
theta = yupi.stats.turning_angles_ensemble(trajs)
yupi.graphics.plot_angles_hist(theta)

# Mean square displacement
msd, msd_std = yupi.stats.msd(trajs, time_avg=True, lag=30)
yupi.graphics.plot_msd(msd, msd_std, dt, lag=30)

# Kurtosis
kurtosis = yupi.stats.kurtosis(trajs, time_avg=False, lag=30)
kurt_ref = yupi.stats.kurtosis_reference(trajs)
yupi.graphics.plot_kurtosis(kurtosis, kurtosis_ref=kurt_ref, dt=dt)

# Velocity autocorrelation function
vacf, _ = yupi.stats.vacf(trajs, time_avg=True, lag=50)
yupi.graphics.plot_vacf(vacf, dt, 50)

# Power Spectral Density
psd_mean, psd_std, omega = yupi.stats.psd(trajs, lag=200, omega=True)

