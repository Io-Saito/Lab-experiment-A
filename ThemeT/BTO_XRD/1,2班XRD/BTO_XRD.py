# %%
import japanize_matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc
from scipy import signal
from scipy.fftpack import fft, fftshift

# %%"
df = pd.read_csv(
    "201209_1班XRD.csv", header=59, delimiter="\t")
display(df.head(10))
theta_si = np.array(df["; 2THETA"])
spectrum_si = np.array(df["Cnt2_D1"])

# %%
fig = plt.figure()
ax1 = fig.add_subplot()
ax1.plot(theta_si, spectrum_si, linewidth=1)
ax1.set_title("Si基板XRD")
ax1.set_xlabel("2θ[°]")
ax1.set_ylabel("ピーク")
ax1.set_yscale("log")
fig.show()

# %%
df2 = pd.read_csv(
    "201209_2班XRD.csv", header=59, delimiter="\t")
theta_sipt = df2["; 2THETA"]
spectrum_sipt = df2["Cnt2_D1"]
fig2 = plt.figure()
ax2 = fig2.add_subplot()
ax2.plot(theta_sipt, spectrum_sipt, linewidth=1)
ax2.set_title("Si-Pt基板XRD")
ax2.set_xlabel("2θ[°]")
ax2.set_ylabel("ピーク")
ax2.set_yscale("log")
fig2.show()

# %%

# 波長
lam = 1.54068*(10**-10)
# 波長2θ→格子定数


def lattice_constant(theta):
    d = lam/(2*np.sin(np.radians(theta/2)))*(10**10)
    return d  # [Å]


display(lattice_constant(70))

# %%
