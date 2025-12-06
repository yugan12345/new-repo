import matplotlib.pyplot as plt
import numpy as np

t_stop = 0
t_release = 5/60  
t = np.linspace(0, 0.5, 200)

v_form = -30 
v_recover = -40 
x_form = v_form * (t - t_stop)

t_rec = np.linspace(t_release, 0.5, 200)
x_rec = v_recover * (t_rec - t_release)

# Compute meeting point
# -30 t_m = -40 (t_m - t_release)
# 10 t_m = 40 t_release
t_m = 4 * t_release
x_m = v_form * (t_m - t_stop)

plt.figure()
plt.plot(t, x_form, label="Backward Forming Shock")
plt.plot(t_rec, x_rec, label="Backward Recovery Shock")
plt.vlines(t_m, x_m-5, x_m+5, linestyles='dashed', label="Stationary Shock Front")

plt.xlabel("Time (hours)")
plt.ylabel("Distance (km, upstream negative)")
plt.title("Time–Distance Diagram of Shockwaves")
plt.legend()
plt.show()
