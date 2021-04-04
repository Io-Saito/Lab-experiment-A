# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import sympy as sp

# %%
df = pd.read_csv("drive-download-20210116T031357Z-001/ryuudou.csv")
df.head(10)
display(df.columns)
df["Unnamed: 0"] = df["Unnamed: 0"].fillna(method="ffill")
koteisou = df["Unnamed: 0"] == "固定層"
senni = df["Unnamed: 0"] == "遷移域"
ryudousou = df["Unnamed: 0"] == "流動層"
kaeri = df["Unnamed: 0"] == "帰り"
f_471 = koteisou | senni
f_473 = ryudousou | kaeri | senni
df_Ryudo_P = df[f_473]
df_Ergun = df[f_471]
df.head(10)

display(df_Ryudo_P["層高さ[cm]"].mean())
# %%


d_p = 4.08/(10**4)  # 粒径
mu = 1.82/(10**5)  # ガス粘度
rho_g = 1.2  # ガス密度
rho_p = 2.58*(10**3)  # 粒子密度
g = 9.8  # 重力加速度
vol_p = 1.286/rho_p  # 粒子体積
D = 0.1  # 反応容器の体積


def kuugeki(L):  # 空隙りつ
    L_f = L/100
    V = (D/2)**2*np.pi*L_f  # 粒子が動ける体積
    e = (V-vol_p)/V  # 空隙率
    return e


def f4_7_1(u_0, L):  # 圧力損失(Ergunの式)
    e_m = kuugeki(L)
    phi_s = 1  # 形状定数(球を仮定)
    delta_P = L/100*((150*mu*u_0*(1-e_m)**2)/((phi_s*d_p)**2*e_m**3) +
                     (1.75*rho_g*u_0**2*(1-e_m))/((phi_s*d_p*e_m**3)))
    return delta_P


def f4_7_3(L_f):  # 流動層での圧損
    e_f = kuugeki(L_f)
    delta_P = L_f*(1-e_f)*(rho_p-rho_g)*g
    return delta_P


# %%


def Reynolds(u):
    Re = d_p*u*rho_g/mu
    return Re


def Re_hantei(umf_pair):
    pair_small = [Reynolds(umf_pair[0]), umf_pair[0]]
    pair_large = [Reynolds(umf_pair[1]), umf_pair[1]]
    # 最小流動化速度・Re数は呼び出しもとで計算する
    # 渡されたRe数を元に正しい最小流動化速度を返す
    if (pair_small[0] < 20):
        print(f"{pair_small[0]}<20：微小粒子。\n最小流動化速度:{pair_small[1]}")
        return pair_small
    elif(pair_large[0] > 1000):
        print(f"{pair_large[0]}>1000：粗大粒子。\n最小流動化速度:{pair_large[1]}")
        return pair_large
    else:
        print("something wrong")

# %%


def f_475_or_476():  # 微小粒子の最小流動化速度
    phi_s = 1
    L_f = 10.5/100
    V = (D/2)**2*np.pi*L_f  # 粒子が動ける体積
    e_mf = (V-vol_p)/V
    u_mf_small = e_mf**3*phi_s**2*d_p**2*(rho_p-rho_g)*g/(150*(1-e_mf)*mu)
    u_mf_large = np.sqrt(e_mf**3*phi_s*d_p*(rho_p-rho_g)*g/(1.75*rho_g))
    return [u_mf_small, u_mf_large]


def f_479_or_4710():
    phi_s = 1
    u_mf_small = d_p**2*(rho_p-rho_g)*g/(1650*mu)
    u_mf_large = np.sqrt(d_p*(rho_p-rho_g)*g/(24.5*rho_g))
    return [u_mf_small, u_mf_large]


    # %%
umf_475 = Re_hantei(f_475_or_476())
umf_479 = Re_hantei(f_479_or_4710())


display(umf_475)
display(umf_479)
# %%

df["delta_p Ergan"] = np.log(f4_7_1(df_Ergun["u[m/s]"],
                                    df_Ergun["層高さ[cm]"]))
df["delta_p Atsuson"] = np.log(f4_7_3(df_Ryudo_P["層高さ[cm]"]))

df["空隙りつ"] = kuugeki(df["層高さ[cm]"])

# %%
df
# %%
fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(111)
ax1.scatter(df["log u"][0:22], df["logΔP"][0:22],
            marker="o", label="行き", facecolor="None", edgecolors='red')
ax1.scatter(df["log u"][23:37], df["logΔP"][23:37],
            label="帰り", marker="D", facecolor="None", edgecolors='blue')
ax1.scatter(df[f_471]["log u"].head(10),
            df["delta_p Ergan"].dropna().head(10), label="式4.7.1(行き)")
ax1.scatter(df[f_471]["log u"].tail(9),
            df["delta_p Ergan"].dropna().tail(9), label="式4.7.1(帰り)")
ax1.scatter(df[f_473]["log u"],
            df["delta_p Atsuson"].dropna(), label="式4.7.3")
ax1.axvline(x=np.log(umf_479[1]), color="black", linestyle="dashed")
ax1.axvline(x=np.log(umf_475[1]), color="black", linestyle="dashed")
ax1.text(np.log(umf_475[1])+0.01, 4.3, "<-最小流動化速度\n(4.7.5)")
ax1.text(np.log(umf_479[1])-0.42, 4.3, "最小流動化速度->\n(4.7.9)")
ax1.legend(loc="lower left")
ax1.set_ylim(4, 8)
ax1.set_yscale("log")
ax1.set_xlabel("log u")
ax1.set_ylabel("log ΔP(log scale)")
ax1.set_title("流速と圧力損失の関係")

# %%
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(df["log u"][0:22], df["空隙りつ"][0:22],
            marker="o", label="行き", facecolor="None", edgecolors='red')
ax1.scatter(df["log u"][23:37], df["空隙りつ"][23:37],
            label="帰り", marker="D", facecolor="None", edgecolors='blue')
ax1.set_xlabel("log u")
ax1.set_ylabel("空隙率")
ax1.legend(loc="upper left")
ax1.set_title("行き・帰りの空隙率の比較")
# %%
