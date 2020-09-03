# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytablewriter


# %%
# 飽和CO2濃度[mol/m^3]
C_A = 41.35

# 検量線のプロット
percent = np.array([1.4, 6.8, 16.0])
# 希釈律
c = np.array([0.1, 0.5, 1])
# 原液モル濃度[mol/m^3]
M = 0.252*1000/(84.01*0.5)
display(M)
# 濃度
conc = M*c
display(conc)

table = np.transpose(np.vstack((conc, percent)))
display(table)
columns = ["モル濃度", "メーターの読み"]
DF = pd.DataFrame(data=table, columns=columns)
display(DF)
writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(DF)
writer.write_table()
# %%
# 直線近似
x = np.linspace(0, 20, 2000)
poly = np.polyfit(percent, conc, 1)
display(poly)
lin = np.poly1d(poly)(x)
fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
ax.scatter(percent, conc, label="experimental value")
ax.set_ylabel("molar concentration ")
ax.set_xlabel("concentration by percent")

ax.plot(x, lin, label="approximation")
ax.legend(loc="upper left")
ax.set_title("calibration curve")
plt.show()
# %%
# 検量線からモル濃度を算出する関数

poly = np.polyfit(percent, conc, 1)
display(poly)


def kenryou(x):
    conc_percent = np.poly1d(poly)(x)
    return conc_percent


# 吸収前濃度
display(kenryou(0.80))
display(kenryou(0))

# 吸収後濃度
meter = [15.7, 10.8, 9.0, 7.2]
concentration = []
for m in meter:
    concentration.append(kenryou(m))
c = np.array(concentration)
display(c)


# %%
# 表面流速と接触時間
# 流量[m^3/s]
Q_L = np.array([0.1, 0.2, 0.3, 0.4])/(10**3*60)
display(Q_L)

# 粘土[Pa s]
mu = 0.00106340

# 密度
rho = 998.67

# 代表長さ[m]
d = 10/10**3

# 液膜レイノルズ数
Re = 4*rho*Q_L/(3.14*d*mu)
display(Re)

# 膜厚
x_L = (3*mu**2/(4*9.8*rho**2))**(1/3)*Re**(1/3)
display(x_L)

pooly = np.polyfit(np.log(Re), np.log(x_L), 1)
display(pooly)

fig = plt.figure(figsize=(6.0, 6.0))
ax = fig.add_subplot(1, 1, 1)
ax.scatter(Re, x_L, label="experimental")
ax.set_xscale("log")
ax.set_ylabel("k")
ax.set_yscale("log")
ax.set_ylim(0.00001, 0.001)
plt.scatter(Re, x_L)
plt.show


# Γ
gamma = Q_L*rho/(3.14*d)

# 表面流速
v = 3*gamma/(2*rho*x_L)
display(v)

# 接触時間
t_c = 140/(1000*v)
display(t_c)

# 拡散係数
D = 1.6052*10**(-9)

# 物質移動係数
k_L_s = 2*np.sqrt(D/(3.14*t_c))  # 時間短い時
k_L_l = 3.412*D/x_L  # 時間長い時
display(k_L_s)
display(k_L_l)


# %%
# 濃度勾配
# 入口濃度
C_1 = 0.5419
# 界面濃度
C_i = 41.3
# 出口濃度


def kL(E):
    kL = gamma*1000/(rho*140)*np.log(1/E)
    return kL


def C_2_calc(k):
    ln_E = k*rho*140/(1000*gamma)
    E = np.exp(-ln_E)
    C_2 = C_i-E*(C_i-C_1)
    return C_2


k_L_HTU = np.array([8.98784342e-05, 8.98784342e-05,
                    8.98784342e-05, 8.98784342e-05])

plot_a = C_2_calc(k_L_s)
plot_b = C_2_calc(k_L_l)
plot_c = C_2_calc(k_L_HTU)


display(plot_a)
display(plot_b)
display(plot_c)

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax1.scatter(Re, c, label="experimental value")
ax1.scatter(Re, plot_c, label="HTU")
ax1.scatter(Re, plot_a, label="short")
ax1.scatter(Re, plot_b, label="long")
ax1.set_xlabel("Re")
ax1.set_ylabel("C2")
ax1.legend(loc="upper right")
ax1.set_title("Re vs C2")
plt.show()

poly = np.polyfit(Re, np.log(np.log(plot_c)), 1)
display(poly)

plt.plot(Re, np.log(np.log(plot_c)))
plt.show()
# %%
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax1.scatter(t_c, k_L_l, label="experimental value")
ax1.set_xlabel("Re")
ax1.set_ylabel("C2")
ax1.legend(loc="upper right")
ax1.set_title("Re vs C2")
plt.show


# %%
