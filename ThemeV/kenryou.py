# %%
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy.optimize import curve_fit
import pandas as pd

# %%
kDa = np.array([150, 100, 80, 60, 50, 40])
mm = np.array([6, 12, 16, 22.5, 26.5, 32.8])

# %%


def func(x, a, b):
    y = 10**(x*a+b)
    return y


# %%
popt, cov = curve_fit(func, mm, kDa)
display(popt)
lin = np.linspace(6, 32.8, 300)

line = func(lin, popt[0], popt[1])
# array([-0.02343557,  2.30343239])
# %%


def molcular_weight(mm):
    y = func(mm, popt[0], popt[1])
    return y


# %%
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(mm, kDa, label="マーカー分子量")
ax1.plot(lin, line, color="orange", label="検量線")
ax1.scatter(11.5, molcular_weight(11.5), label="βガラクトシダーゼ(実験値)", color="red")
ax1.set_yscale("log", basey=10)
ax1.legend(loc="upper right")
ax1.set_xlabel("泳動距離[mm]")
ax1.set_ylabel("分子量[kDa]")
ax1.set_title("検量線")
fig.show()

# %%


# %%
display(molcular_weight(11.5))

# %%
DataFrame = pd.DataFrame([[15, 0.107], [122, 0.064]], columns=[
                         'time', 'abs'], index=['A', 'B'])

DataFrame["abs_600"] = [0.623, 0.681]
display(DataFrame)
# %%


def Lambert_Beer(OD):
    coef = 0.0045  # 吸光係数
    dist = 1  # 光路長
    vol = 2  # 溶液の体積
    conc = OD/(coef*dist*vol)
    nmol = conc*vol  # 合成量[nmol]
    return nmol


def kassei(time, OD_420, OD_600):
    Fungus = OD_600  # 吸光度測る時は十倍希釈されてるので
    vol = 0.1  # 100μl使ったので0.1[mL]
    kassei = Lambert_Beer(OD_420)/(time/60*Fungus*vol)
    return kassei


# %%
display(kassei(DataFrame["time"], DataFrame["abs"], DataFrame["abs_600"]))

DataFrame["kassei"] = kassei(
    DataFrame["time"], DataFrame["abs"], DataFrame["abs_600"])
# %%
DataFrame
# %%
