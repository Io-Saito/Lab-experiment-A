# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import matplotlib as mpl
from matplotlib import rc
from scipy import signal
from scipy.fftpack import fft, fftshift
rc('text', usetex=True)
# %%
df = pd.read_csv("ZnO_UV-Vis.csv", header=2).dropna(how="any")
wl = np.array(df["Wavelength (nm)"])
Ab = np.array(df["Absorbance (a.u.)"])
# %%
fig = plt.figure()
ax1 = fig.add_subplot()
ax1.plot(wl, Ab)
ax1.set_title("ZnO UV-Vis Spectrum")
ax1.set_xlabel("Wavelength [nm]")
ax1.set_ylabel("Absorbance(a.u.)")
fig.show()

# %%
# 定数
c = 299792458
hbar = 6.582119569*(10**-16)
# %%
x = 2*np.pi*c*hbar/(wl*(10**-9))
y = x**2*Ab**2
maxId = signal.argrelmax(y)[0].tolist()
minId = signal.argrelmin(y)
display(x[132])


# %%
lin = np.linspace(3.15, 3.45, 100)
poly = np.polyfit(x[132:162], y[132:162], 1)
line = np.poly1d(poly)(lin)
display(poly)
x_lim = poly[1]/poly[0]
display(x_lim)
# バンドギャップ＝3.2[eV]
# %%
fig = plt.figure()
ax1 = fig.add_subplot()
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.plot(x, y)
ax1.scatter(x[132], y[132], color="red")
ax1.scatter(x[162], y[162], color="red")
ax1.plot(lin, line, color="orange")
ax1.set_title("ZnO tauc plot")
ax1.set_xlabel(r"$\hbar\omega[eV]$")
ax1.set_ylabel(r"$(\hbar \omega \alpha)^2$")
ax1.text(3.05, -0.1, r"$E_G=3.18[eV]$")
fig.show()

# %%
