# %%
import matplotlib.pyplot as plt
import numpy as np
# %%
# Re数
Re = np.array([5000, 10000, 20000, 30000])
mu = 1.86/(10**5)
rho = 1.18
d = 22/1000

# 流速を求める
u = Re*mu/(rho*d)
display(u)
# %%
# 体積流量を求める
# 管の断面積[m^2]
S = np.pi*((d/2)**2)
display(S)
# V[m^3/s]
V = S*u
display(V)
# V[l/min]
V_min = V*1000*60
display(V_min)
# オリフィス係数
oliphis = [6.721/100, 1.343/100, 1.664/1000, 3.993/10000, 6.179/100000]
# 各オリフィス使用時の液柱差を各Re数について求める[cm]
# mで出てくるので　100倍する
# L/min換算
for i, r in enumerate(oliphis):

    H = (293/273)*r*(V_min**2)
    display("オリフィスA"+str(i), "液柱差："+str(H))

# %%
# 各種定数

d = 22/(10**3)
l = 1.3
mu = 1.86/(10**5)
mu_wall = 2.24/(10**5)

# 乱流のときRe-Nu関係式


def McAdams(Re, Pr):
    Nu = 0.023*(Re**0.8)*(Pr**0.4)
    return Nu


# 層流のときRe-Nu関係式


def Laminar(Re, Pr):
    Nu = 1.86*(Re**(1/3))*(Pr**(1/3))*((d/l)**(1/3))*((mu/mu_wall)**0.14)
    return Nu


Pr = 1.015*1000*(21.76/10**6)/0.0318
# 層流域Re　
Re_1 = np.array([10, 50, 100, 500, 1000, 1500, 2000, 2100])
Re_1_ = np.array([2500, 5000])
Re_2_ = np.array([5000, 6000, 7000, 8000])
Re_2 = np.array([10000, 20000, 30000, 50000, 70000, 100000, 120000])

# %%
fig = plt.figure()
ax1 = fig.add_subplot()
ax1.plot(Re_1, Laminar(Re_1, Pr), label="Laminar", color="blue")
ax1.plot(Re_1_, Laminar(Re_1_, Pr), label="Laminar",
         color="blue", linestyle="dotted")
ax1.plot(Re_2_, McAdams(Re_2_, Pr), label="Turblamce",
         color="red", linestyle="dotted")
ax1.plot(Re_2, McAdams(Re_2, Pr), label="Turblamce",
         color="red")
ax1.set_yscale('log')
ax1.set_xscale('log')
ax1.legend(loc="upper left")
ax1.set_title("Re-Nu plot")
ax1.set_xlabel("Re")
ax1.set_ylabel("Nu")
fig.show()

# %%
# 空気側の熱伝達係数
# 空気の熱伝導率
display(Laminar(5000, 0.7))
display(McAdams(5000, 0.7))
display(McAdams(30000, 0.7))

# %%
