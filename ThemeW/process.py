# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
from scipy.optimize import curve_fit
from scipy import signal
# %%
# データ読み込み
df_step = pd.read_table(
    "/Users/io/Documents/課題/6semester/実験B/ThemeX/drive-download-20210116T031357Z-001/Step_20201223_3.txt", names=["time", "T", "Q"], skiprows=1)
df_P = pd.read_table("/Users/io/Documents/課題/6semester/実験B/ThemeX/drive-download-20210116T031357Z-001/３日目/20201224_3_P_Control.txt",
                     names=["time", "T", "Q"], skiprows=1)
df_PID = pd.read_table("/Users/io/Documents/課題/6semester/実験B/ThemeX/drive-download-20210116T031357Z-001/３日目/20201224_3_PID_Control.txt",
                       names=["time", "T", "Q"], skiprows=1)
df_M = pd.read_table("drive-download-20210116T031357Z-001/３日目/20201224_3_Manual_Control.txt",
                     names=["time", "T", "Q"], skiprows=1)

# %%
# 各種定数・物性値
wp = 1.286  # 充填粒子流量
D = 0.1  # 流動層の直径
C_pp = 770  # 物性値
C_pg = 1003  # 物性値
rho_g = 1.2  # ガス密度
u0 = 0.13/(60*((D/2)**2*np.pi))  # 流速
Lf = 10.96/100  # 流動層の高さ[m](流動層の実験の流動状態＆帰りを平均)
rho_p = 2.58*(10**3)  # 粒子密度
vol_p = wp/rho_p  # 粒子体積
V = (D/2)**2*np.pi*Lf  # 粒子が動ける体積
ef = (V-vol_p)/V
U = 20  # 物性値(伝熱系数)
A = np.pi*D*Lf  # 伝熱面積


# %% 課題の式


def f_4732():
    tau_p = (wp*C_pp+(np.pi*D**2*Lf*ef*rho_g*C_pg/4)) / \
        (U*A+(np.pi*D**2*rho_g*C_pg*u0/4))
    K_p = 1/(U*A+(np.pi*D**2*rho_g*C_pg*u0/4))
    K_d1 = (np.pi*D**2*rho_g*C_pg*u0/4)/(U*A+(np.pi*D**2*rho_g*C_pg*u0/4))
    K_d2 = U*A/(U*A+(np.pi*D**2*rho_g*C_pg*u0/4))
    return {"tau_p": tau_p, "K_p": K_p, "K_d1": K_d1, "K_d2": K_d2}


def f_4725_4726(PID):
    if PID == False:
        Kc = tau_p*(1+td/(3*tau_p))/(Kp*td)
        tau_1 = "inf"
        tau_d = 0
    else:
        Kc = tau_p*(4/3+td/(4*tau_p))/(Kp*td)
        tau_1 = (32+6*td/tau_p)*td/(13+8*td/tau_p)
        tau_d = 4*td/(11+2*td/tau_p)
    return {"K_c": Kc, "tau_1": tau_1, "tau_d": tau_d}


def offset():  # 最後から5ばんめの値を平均した物を設定値からひく
    t_inf = df_P.tail(5).mean()
    offset = 40-t_inf["T"]
    return offset


def PID():  # PID制御のオーバーシュート、振幅減衰比、応答時間、制定時間を求める
    set_point = 40  # 設定値
    Tr = df_PID[df_PID["T"] > set_point].head(1)["time"]  # 応答時間
    A = df_PID.nlargest(1, "T")  # 図477A
    B = set_point-(df_PID["T"].loc[0])  # 図477B
    epsilon = set_point*0.05  # 偏差が5%以内
    Ts = df_PID[(set_point - epsilon > df_PID["T"]) |
                (df_PID["T"] > set_point + epsilon)]  # 収束時間以外の部分
    if Ts.tail(1).index < Tr:
        Ts = 0  # もし、偏差5%を超えてる部分がない時は収束時間を0とする
    else:
        Ts = Ts.tail(1).index
    overshoot = (A["T"]-set_point)/B
    return{"overshoot": overshoot, "Ts": Ts, "Tr": Tr}


def Step(t, t_d, Kp, tau_p):
    y = Kp*(1-np.exp(-(t-t_d)/tau_p))*df_step["Q"][0]+df_step["T"][0]
    # Y.append(y)
    return y


time = df_step["time"].to_numpy()
temp = df_step["T"].to_numpy()
popt, pcov = curve_fit(
    Step, time, temp)

params = f_4732()
display(params)
# tau_p = params.get("tau_p")
# Kp = params.get("K_p")
# td = popt[0]

tau_p = popt[2]
Kp = popt[1]
td = popt[0]

# %%
display(f_4725_4726(PID=True))
display(f_4725_4726(PID=False))
display(f_4732())
display(offset())
display(PID())

display(df_M.len)
df_M["counter"] = a
# %%
A = np.array([380, 520, 550, 750, 1010, 1100, 1200, 1360, 1500, 1750])
list = []
list2 = []
list3 = []
for a in A:
    b = df_M["Q"].to_numpy()[a]
    c = df_M["T"].to_numpy()[a]
    tup = (a, b)
    tup2 = (a+2, b+2)
    tup3 = (a, c+3)
    list.append(tup)
    list2.append(tup2)
    list3.append(tup3)


# %%

list
# %%
#　プロット
fig_step = plt.figure(figsize=(12, 12))
ax_step_T = fig_step.add_subplot(221)
ax_step_Q = fig_step.add_subplot(222)
ax_step_T.plot(df_step["time"], df_step["T"], label="実測値")
ax_step_T.plot(time, Step(
    time, popt[0], popt[1], popt[2]), label="フィッティング")
ax_step_T.plot(time, Step(
    time, popt[0], Kp, tau_p), label="4.7.32式")
ax_step_Q.plot(df_step["time"], df_step["Q"])
ax_step_T.set_ylim([10, 40])
ax_step_T.set_xlabel("時間[s]")
ax_step_Q.set_xlabel("時間[s]")
ax_step_T.set_ylabel("温度[℃]")
ax_step_Q.set_ylabel("熱量")
fig_step.suptitle("ステップ応答")
ax_step_T.legend(loc="lower right")

fig_P = plt.figure(figsize=(12, 12))
ax_P_T = fig_P.add_subplot(221)
ax_P_Q = fig_P.add_subplot(222)
ax_P_T.plot(df_P["time"], df_P["T"])
ax_P_Q.plot(df_P["time"], df_P["Q"])
ax_P_T.set_ylim([0, 50])
ax_P_T.set_xlabel("時間[s]")
ax_P_Q.set_xlabel("時間[s]")
ax_P_T.set_ylabel("温度[℃]")
ax_P_Q.set_ylabel("熱量")
fig_P.suptitle("P制御")

fig_PID = plt.figure(figsize=(12, 12))
ax_PID_T = fig_PID.add_subplot(221)
ax_PID_Q = fig_PID.add_subplot(222)
ax_PID_T.plot(df_PID["time"], df_PID["T"])
ax_PID_Q.plot(df_PID["time"], df_PID["Q"])
ax_PID_T.scatter(845, 38, marker="^", color="black")
ax_PID_T.scatter(1235, 38, marker="^", color="black")
ax_PID_T.set_ylim([0, 50])
ax_PID_T.set_xlabel("時間[s]")
ax_PID_Q.set_xlabel("時間[s]")
ax_PID_T.set_ylabel("温度[℃]")
ax_PID_Q.set_ylabel("熱量")
fig_PID.suptitle("PID制御")

fig_M = plt.figure(figsize=(12, 12))
ax_M_T = fig_M.add_subplot(221)
ax_M_Q = fig_M.add_subplot(222)
ax_M_T.plot(df_M["time"], df_M["T"])
ax_M_Q.plot(df_M["time"], df_M["Q"])
for i, r in enumerate(list3):
    ax_M_T.annotate(i+1, xy=r, color="black")
ax_M_T.scatter(1002, 38, marker="^", color="black")
ax_M_T.scatter(1363, 38, marker="^", color="black")
for i, r in enumerate(list2):
    ax_M_Q.annotate(i+1, xy=r, color="black")
ax_M_T.set_ylim([0, 50])
ax_M_T.set_xlabel("時間[s]")
ax_M_Q.set_xlabel("時間[s]")
ax_M_T.set_ylabel("温度[℃]")
ax_M_Q.set_ylabel("熱量")
fig_M.suptitle("手動制御")

# %%
