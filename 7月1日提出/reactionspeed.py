# %%%
import numpy as np
import scipy as sci
import sympy as sym
import matplotlib.pyplot as plt
import pandas as pd
import pytablewriter
# %%
# HClの力価
f = 0.997
# NaOH標定の解析
# 標定に使ったNaOHの平均体積
V_NaOH_ = np.mean([11.00, 10.97, 10.98, 11.05])
# 時間
time = np.array([0, 300, 600, 900, 1200, 1500, 1800])
# これは0.1MのHCl10ｍL(f=0.997)の滴定に使った量
conc_NaOH = 0.1*10*f/V_NaOH_
# 滴定したNaOH容量
V_NaOH = np.array([21.9, 23.0, 23.55, 24.0, 24.35, 24.62, 24.85])
# 余剰HCl=滴定で中和されたHCl
HCl_surplus = V_NaOH*conc_NaOH/(1000*f)
# 反応液50ｍLと中和したHCl[mol]
HCl_used = 0.1*25/1000-HCl_surplus
# 反応液中のOH^-濃度
conc_OH = HCl_used*1000*f/50
# AcO^-濃度
conc_AcO = 60*conc_NaOH/500-conc_OH
# AcOEt初濃度　体積と比重と分子量から
conc_AcOEt_0 = 0.4*0.902*1000/500.4/88.11
# %%
# OH^-初濃度とAcOEt初濃度の差
print(60*conc_NaOH/500 - conc_AcOEt_0)
# AcOEt濃度
conc_AcOEt = conc_AcOEt_0-conc_AcO
# lnのやつ
ln = np.log(np.divide(conc_OH, conc_AcOEt))
# %%
table = np.transpose(np.vstack(
    (time, V_NaOH, HCl_surplus, HCl_used, conc_OH, conc_AcO, conc_AcOEt, ln)))
print(table)


# %%
columns = ["time", "V_NaOH", "HCl_surplus", "HCl_used",
           "conc_OH", "conc_AcO", "conc_AcOEt", "ln"]
df = pd.DataFrame(data=table, columns=columns)
print(df)

writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(df)
writer.write_table()
# %%
# 線形近似
x = time
y = ln
poly = np.polyfit(x, y, 1)
print(poly)
linear = np.poly1d(poly)(x)
# %%
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax1.scatter(time, ln)
ax1.plot(time, linear)
ax1.set_title("reaction speed culculated by integration")
ax1.set_xlabel("time[s]")
ax1.set_ylabel("ln([OH^-]/[AcOEt])[-]")
plt.show()


# %%
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax1.scatter(time, conc_OH, color='red', label='OH')
ax1.scatter(time, conc_AcOEt, color="blue", label="AcOEt")
ax1.set_title("reaction speed culculated by integration")
ax1.set_xlabel("time[s]")
ax1.set_ylabel("conc[M]")
ax1.legend(loc="upper left")
plt.show()


# %%
HCl_used

# %%
conc_AcO

# %%
