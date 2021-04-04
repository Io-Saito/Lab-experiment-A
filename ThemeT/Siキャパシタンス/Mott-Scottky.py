# %%
import japanize_matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc
rc('text', usetex=True)
print(mpl.get_configdir())
print(mpl.matplotlib_fname())
# %%
df = pd.read_csv("3,4Cp_Rp.csv").dropna(how="any")
Cp = np.array(df["Co"])  # 単位[F]
V = np.array(df["BIAS"])  # 単位[V]
Cd = Cp/0.04
display(Cd)
# %%
# 近似
lin = np.linspace(-10, -4, 100)
poly = np.polyfit(V, 1/(Cd**2), 1)
line = np.poly1d(poly)(lin)
display(poly[0])
# %%
fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.scatter(V, 1/(Cd**2), label="experimental value")
ax1.plot(lin, line, color="orange", label="approximation")
ax1.legend(loc="upper right")
ax1.set_title("Mott-Scottky plot")
ax1.text(-9, 2.3e+17, "y=-3.46x+1.73")
ax1.set_xlabel("BIAS[V]")
ax1.set_ylabel(r"$\frac{1}{C_D^2}$", fontsize=12)
fig.show()

# %%
# 電気素量:1.602*10^-19
# 真空の誘電率:8.85*10^-12
Nd = -2/(poly[0]*11.7*1.602*(10**-19)*8.85*(10**-12)/100)
display(Nd/(10**14))
# Nd=3.49*10^-14

# %%
