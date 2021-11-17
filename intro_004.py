import numpy as np
import yupi.stats
import yupi.graphics
from yupi.generators import LangevinGenerator

np.random.seed(0)

T = 500     # Total time (number of time steps if dt==1)
dim = 2     # Dimension of the walker trajectories
N = 500       # Number of random walkers
dt = 0.5    # Time step

tau = 2               # Relaxation time
sigma = 0.1     # Scale of the noise pdf


lg = LangevinGenerator(T, dim, N, dt, tau, sigma)
trajs = lg.generate()


# Spacial trajectories
yupi.graphics.plot_2D(trajs[:10], legend=False)

#  velocity histogram 
v = yupi.stats.speed_ensemble(trajs, step=1)
yupi.graphics.plot_velocity_hist(v, bins=20)

#  turning angles 
theta = yupi.stats.turning_angles_ensemble(trajs)
yupi.graphics.plot_angles_hist(theta)

#  mean square displacement 
msd, msd_std = yupi.stats.msd(trajs, time_avg=True, lag=30)
yupi.graphics.plot_msd(msd, msd_std, dt, lag=30)

#  kurtosis
ref = yupi.stats.kurtosis_reference(trajs)
kurtosis = yupi.stats.kurtosis(trajs, time_avg=False, lag=30)
yupi.graphics.plot_kurtosis(kurtosis, kurtosis_ref=ref, dt=dt)

#  velocity autocorrelation function 
vacf, _ = yupi.stats.vacf(trajs, time_avg=True, lag=50)
yupi.graphics.plot_vacf(vacf, dt, 50)

# power spectral density
psd_mean, psd_std, omega = yupi.stats.psd(trajs, lag=150, omega=True)
yupi.graphics.plot_psd(psd_mean, omega, psd_std)