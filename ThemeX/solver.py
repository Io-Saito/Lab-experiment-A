# %%
import numpy as np
from scipy import optimize
import pandas as p
# %%
# 設計方程式に基づく反応率の算出
# パラメーター
F_A0 = 10*1000/30.07  # feed流量[mol/s]
l = np.linspace(1, 100, 100)  # 長さ:変動する時
r = np.linspace(0.001, 0.15, 100)  # 直径:変動する時
t = np.linspace(801, 900, 100)
R = 0.05  # 直径:固定値
L = 10  # 長さ:固定値
x_A = np.linspace(0.000, 1, 100000)  # 有効数字4けたで反応率を求める
R_conc = 8.314  # 気体定数
P = 0.5*(10**6)  # feed圧力

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
display(l)
# %%


def PV_NRT(T):  # feedエチレン組成
    C_A0 = P/(R_conc*(T+273))
    return C_A0


def Ahrenius(T):  # 反応速度定数
    k = 6.193*10**16*np.exp(-3.43*(10**5)/(R_conc*(T+273)))
    return k


def volume(r, l):  # 管の体積
    V = l*((r/2)**2)*np.pi*100
    return V


def func(x_A, V, T):  # 反応率の関数
    C_A0 = PV_NRT(T)
    k_a = Ahrenius(T)
    y = (2*np.log(1/(1-x_A))-x_A)-(k_a*C_A0*V/F_A0)
    return y


def ans(v, T):  # 求根 func=Vになるx_Aを求めたい
    list = []
    for x in x_A:
        y = func(x, v, T)
        list.append([x, np.abs(y)])
    array = np.array(list)
    # yの値にしたがって並べ替える
    array_sort = array[np.argsort(array[:, 1])]
    return array_sort[0, 0]


# %%
List_T = []
for T in t:
    List_T.append(ans(volume(R, L), T))
    display(ans(volume(R, L), T))
display(List_T)

# %%
List_R = []
for r_ in r:
    A = ans(volume(r_, L), 845)
    List_R.append(A)
    display(A)
display(List_R)

# %%
List_L = []
for l_ in l:
    A = ans(volume(R, l_), 845)
    List_L.append(A)
    display(A)


# %%
display(List_L)

# %%
