# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %%

# 吸収後濃度
c = np.array([5.98684539, 4.19766519, 3.54041532, 2.88316545])

# 濃度勾配
# 入口濃度
C_1 = 0.5419

# 界面濃度
C_i = 41.3

# CO2無次元濃度
E = (C_i-c)/(C_i-C_1)
display(E)

gamma = Q_L*rho/(3.14*d)


def kL(E):
    kL = gamma*1000/(rho*140)*np.log(1/E)
    return kL


# %%
# 無次元濃度から求めたkL
kL_exp = kL(E)
display(kL_exp)

# 粘土[Pa s]
mu = 0.00106340

# 密度
rho = 998.67

# 代表長さ[m]
d = 10/10**3

# 表面張力[N/m]
delta = 73.093/1000

# 拡散係数
D = 1.6052*10**(-9)

# Γ
gamma = Q_L*rho/(3.14*d)

# 流動状態の判別
# シュミット数
Sc = mu/(rho*D)
display(Sc)
# ガリレオ数
Ga = rho**2*9.8*(140/1000)**3/mu**2
display(Ga)
# 層流→疑層流　臨海Re数
Re_shift = 93.3*Sc**(-0.24)*Ga**(0.08)*(delta/72)**0.3
display(Re_shift)

# Re数
Re = np.array([199.39049006, 398.78098013, 598.17147019, 797.56196025])

# 各流量のHTU求める
HTU_L = 2.36*Re*Sc**0.5/((rho**2*9.8/mu**2)**(1/3))
display(HTU_L)

# 液側物質移動係数kL
kL_HTU = gamma/(HTU_L*rho)
display(kL_HTU)

# %%
# 実験から液側物質移動係数を求める
kL_exp = kL(E)
display(kL_exp)

# 理論値
kL_theo = np.array([6.70537011e-05, 8.44823695e-05,
                    9.67081716e-05, 1.06441116e-04])

kL_theo_long = np.array(
    [2.11758993e-05, 1.68073224e-05, 1.46825485e-05, 1.33399806e-05])

x_L = np.array([0.00025864, 0.00032587, 0.00037302, 0.00041057])

# 表面流速
v = 3*gamma/(2*rho*x_L)
display(v)

# 接触時間
t_c = 140/(1000*v)
display(t_c)


# %%

poly = np.polyfit(np.log(t_c), np.log(kL_exp), 1)
display(poly)
# プロット
fig = plt.figure(figsize=(6.0, 6.0))
ax = fig.add_subplot(1, 1, 1)
ax.scatter(t_c, kL_exp, label="experimental")
ax.scatter(t_c, kL_HTU, label="HTU")
ax.scatter(t_c, kL_theo, label="theoretical short")
ax.scatter(t_c, kL_theo_long, label="theoretical long")
ax.set_xlabel("t")
ax.set_xscale("log")
ax.set_ylabel("k")
ax.set_yscale("log")
ax.set_ylim(0.00001, 0.001)
plt.legend(loc="upper right")
plt.title("Contact time vsMass transfer coefficient")
plt.show


# %%
