# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
# 各種定数・データセット
# Re数
Re = np.array([5000, 10000, 20000, 30000])
# 壁からの距離(mm)
r = np.array([11.0, 10.0, 9.0, 8.0, 7.0, 6.0,
              5.0, 4.0, 3.0, 2.0, 1.0, 0.0])
# 温度分布(Re＝5000,10000,20000,30000)
theta = np.array([[98.1, 94.8, 84.0, 80.9, 78.9, 77.3,
                   76.4, 75.4, 74.6, 74.1, 73.9, 73.6],
                  [93.6, 87.6, 78.8, 76.7, 75.4, 73.8,
                   72.6, 71.8, 71.2, 71.0, 70.7, 70.9],
                  [85.1, 77.2, 74.0, 72.3, 69.8, 68.3,
                   67.2, 66.2, 65.3, 64.8, 64.6, 64.5],
                  [75.0, 71.8, 69.7, 67.8, 66.0, 64.8,
                   63.7, 63.1, 62.1, 61.8, 61.7, 61.7]])

# 最大流速[m/s](Re=5000,10000,20000,30000)
u = np.array([3.582, 7.165, 14.33, 21.49])
u_ = np.array([3.582, 14.33])
# 速度比を求める時に使うn
n = np.array([6, 7, 7, 7])
# 管内半径（mm）
R = 11
# 入り口の空気の温度(開始時)
theta_i = np.array([24.4, 21.6])
# 入り口の空気の温度(終了時)
theta_f = np.array([24.8, 22.3])
# θ1:入り口の空気の温度(平均)
theta_1 = (theta_i+theta_f)/2

# 比熱(@20,30,40,50,60℃)
cp_air = np.array([1.003, 1.004, 1.006, 1.007, 1.009])

# 空気の密度(@20,30,40,50,60℃)
rho_air = np.array([1.2042, 1.1645, 1.1273, 1.0924, 1.0596])

# 蒸気の温度
theta_V = 100

lambda_L = 0.682  # 水の伝熱係数
rho_L = 958.38  # 水の密度
g = 9.8  # 重力加速度
mu_L = 0.2821  # 水の粘度
l = 1.3  # 管の長さ
h = 2257  # 蒸発潜熱
d1 = 22/1000  # 内径[m]
d2 = 25/1000  # 外径[m]
lambda_air = 0.0272/1000  # 空気の熱伝導率
lambda_copper = 398  # 銅の熱伝導率

# Pr@50℃
Pr = 1.007*1000*(19.51/10**6)/0.028
display(Pr)


mu = 1.86/(10**5)
mu_wall = 2.24/(10**5)
# %%
# 各種関数


def cp_temp(array, temp):  # その温度における比熱/密度を求める
    list = []
    for t in temp:
        r = 2
        while r <= 6:
            if r*10-5 < t <= r*10+5:
                cp = float(array[r-2])
                list.append(cp)
            else:
                pass
            r = r+1
    cp_list = np.array(list)
    return cp_list


print(cp_temp(rho_air, theta_1))


def ratio(r, Re):  # 速度比(u/umax)求める
    u_umax = ((R-r)/R)**(1/n[Re])
    return u_umax


def vartical_theta(r, Re):  # 縦軸(ruθ/umax)求める
    y = r*theta[Re]*ratio(r, Re)
    return y


def vartical_u(r, Re):  # 縦軸(ru/umax)求める
    y = r*ratio(r, Re)
    return y


def integral(array1, array2):  # 積分(1:横軸,2:縦軸)
    # 点の数を求める
    n = len(array1.tolist())
    # 両端の三角形の合計
    tri = (array2[1]*(array1[0]-array1[1]) +
           array2[-1]*(array1[-2]-array1[-1]))/2
    # その他の台形の面積の合計
    r = 0
    list = []
    for r in range(1, n-1):
        trap = (array2[r]+array2[r+1])*(array1[r]-array1[r+1])/2
        list.append(trap)
        r = r+1
    int = sum(list)+tri
    return int


def McAdams(Re, Pr):  # 乱流のときRe-Nu関係
    Nu = 0.023*(Re**0.8)*(Pr**0.4)
    return Nu


def Laminar(Re, Pr):  # 層流のときRe-Nu関係式
    Nu = 1.86*(Re**(1/3))*(Pr**(1/3))*((d1/l)**(1/3))*((mu/mu_wall)**0.14)
    return Nu


def h_air(Re, Mc):  # 空気がわ熱伝達係数（層流：True）
    if Mc == True:
        h_i = Laminar(Re, Pr)*lambda_air/d1
    else:
        h_i = McAdams(Re, Pr)*lambda_air/d1
    return h_i


def U_theo(Re, Mc, h0, *args):
    theo_1 = (np.pi*d2*l)/((np.pi*d1*l) * (h_air(Re, Mc)))
    print("空気側対流伝熱:", theo_1)
    theo_2 = (np.pi*d2*l)*np.log(d2/d1)/(2*np.pi*l*lambda_copper)
    print("銅の伝熱:", theo_2)
    theo_3 = 1/h0
    print("蒸気側対流伝熱:", theo_3)
    U_theo = 1/(theo_1+theo_2+theo_3)
    return U_theo


# %%
# 算出
g_s = np.array([0.06102, 0.2388])  # 凝縮速度[g/s]

Q_s = g_s/1000*h
print("蒸気の失った熱量:", Q_s)
# 課題２
# θav2:出口の空気の平均温度
theta_av2 = np.array([integral(
    r, vartical_theta(r, 0))/integral(r, vartical_u(r, 0)), integral(
    r, vartical_theta(r, 3))/integral(r, vartical_u(r, 3))])
print("θ2av(出口温度):", theta_av2)
print("θ1(入り口温度):", theta_1)
# 課題３
# 入り口と出口の平均温度
Q = (theta_av2-theta_1)*cp_temp(cp_air, (theta_1+theta_av2)/2) * \
    cp_temp(rho_air,  np.array([20, 20]))*u_*np.pi*(R/1000)**2
print("空気に供給された熱量", Q)
print("空気の密度", cp_temp(rho_air, np.array([20, 20])))
print("入り口と出口の平均温度", (theta_1+theta_av2)/2)
# 課題４
Q1 = Q_s-Q
print("熱損失量", Q1)
# 課題５
# Δθ:対数平均温度差
delta_theta = ((theta_V-theta_1)-(theta_V-theta_av2)) / \
    np.log((theta_V-theta_1)/(theta_V-theta_av2))
print("対数平均温度差:", delta_theta)
# U2:総括伝熱係数
U_2 = Q/(delta_theta*(np.pi*(25/1000)*1.3))
print("総括伝熱係数:", U_2)
# 課題6
# h_i:空気側熱伝達係数
h_i_S = h_air(Re[0], Mc=True)
h_i_L = h_air(Re[1:], Mc=False)
print("空気側熱伝達係数(5000):", h_i_S)
print("空気側熱伝達係数(10000~):", h_i_L)
# 課題7
# h_0:蒸気側熱伝達係数
h_0 = 0.95*(lambda_L**3*rho_L**2*g*l/(mu_L*(g_s/1000)))**(1/3)
print("蒸気側熱伝達係数:", h_0)
# 課題8
# 総括伝熱係数の理論値

# Re:5000,層流
Re_5000_1 = U_theo(5000,  True, h_0[0])
Re_5000_2 = U_theo(5000,  False, h_0[0])
Re_30000_2 = U_theo(30000, False, h_0[1])
print("Re:5000,層流,総括熱伝導率:", Re_5000_1)
print("Re:5000,乱流,総括熱伝導率:", Re_5000_2)
print("Re:30000,乱流,総括熱伝導率:", Re_30000_2)
# %%
# r-θグラフ
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(r, theta[0], label="Re:5000")
ax1.plot(r, theta[3], label="Re:30000")
ax1.legend(loc="upper left")
fig.show()

# %%
# ruθ/u_umax
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(r, vartical_theta(r, 0), label="Re:5000")
# ax1.plot(r, vartical_theta(r, 1), label="Re:10000")
# ax1.plot(r, vartical_theta(r, 2), label="Re:20000")
ax1.plot(r, vartical_theta(r, 3), label="Re:30000")
ax1.legend(loc="upper left")
ax1.set_xlabel("r")
ax1.set_ylabel("θur/u_max")
ax1.set_title("θur/u_max - r graph")
fig.show()


# %%
# ru/u_umaxグラフ
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(r, vartical_u(r, 0), label="Re:5000")
# ax1.plot(r, vartical_u(r, 1), label="Re:10000")
# ax1.plot(r, vartical_u(r, 2), label="Re:20000")
ax1.plot(r, vartical_u(r, 3), label="Re:30000")
ax1.legend(loc="upper left")
ax1.set_xlabel("r")
ax1.set_ylabel("u/u_max")
ax1.set_title("ru/u_max - r graph")
fig.show()

# %%
