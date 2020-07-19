# %%
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from scipy.optimize import curve_fit
import pandas as pd
import pytablewriter
# %%
# ベンゼン質量[g]
be = 96.58-61.67
print(be)
# ベンゼン分子量
w_be = 78.11
# ナフタレン質量[g](あってた)
na = np.array([0.19, 0.19+0.13, 0.19+0.13+0.15])
# 溶液濃度[g/kg](あってた？)
conc = 1000*np.divide(na, be)
print(conc*1000/120)
# %%
# 凝固点降下(あってた)
freezing_point = np.subtract(np.array([1.46, 1.62, 1.80]), 1.23)
print(freezing_point)

# 分子量計算
mol_weight = conc*5.12/freezing_point
print(mol_weight)
# %%
# 線形近似のパターン
# 原点とおる


def func1(x, a):
    return a*x


def func2(x, a, b):
    return a*x+b


# 凝固点降下の線形近似
x_latent = np.linspace(0, 1, 1000)
popt, pcov = curve_fit(func1, na, freezing_point)
print(popt)
linear = popt*x_latent

# 分子量の線形近似
x_latent2 = np.linspace(0, 15, 1000)
popt2, pcov2 = curve_fit(func2, conc, mol_weight)
print(popt2)
linear2 = popt2[0]*x_latent2+popt2[1]


# %%
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax1.scatter(na, freezing_point, label="experimental value")
ax1.plot(x_latent, linear, label="linear approximation")
ax1.set_xlabel("mass of naphtaren[g]")
# ax.set_xlim(0, 0.015)
ax1.set_ylabel("delta T[K]")
ax1.set_title("depression of freezing-point")
ax1.legend(loc="upper left")

ax2 = fig.add_subplot(1, 2, 2)
ax2.scatter(conc, mol_weight, label="experimental value")
ax2.set_title("mol weight and concentration")
ax2.set_xlabel("concentration of naphtaren[g/kg]")
ax2.set_ylim(100, 150)
ax2.set_ylabel("mol_weight")
ax2.plot(x_latent2, linear2, label="linear approximation")
plt.show()


# %%
print(5.12/(1.2422*be/1000))


# %%
table = np.transpose(np.vstack((na, conc, freezing_point, )))
print(table)
columns = ["ナフタレン質量", "ナフタレン質量濃度[g/kg]", "凝固点降下"]
df = pd.DataFrame(data=table, columns=columns)
writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(df)
writer.write_table()


# %%
