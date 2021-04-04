# %%
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# %%
bp = np.array([125, 564, 2332, 4361, 6557, 9416, 23130])
dist = np.array([19.5, 17.2, 11.5, 9.1, 7.0, 6.1, 4.8])

# %%


def curve(x):
    return np.exp(x)


# %%
bp_log = np.log(bp)
bp_point = np.polyfit(dist, bp_log, 1)
line_x = np.linspace(0, 20, 100)
bp_line = np.poly1d(bp_point)(line_x)


# %%
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.scatter(dist, bp, label="kenryou")
ax1.plot(line_x, bp_line)
ax1.set_yscale("log")
fig.show()

# %%
