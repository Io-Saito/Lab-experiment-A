import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def eq(a, b, P, x):
    K_p = x/((1-x)*np.sqrt((b-(a*x/2))/(100-(a*x)/2)*P))
    return K_p


def b_and_p(T):
    log_K_p = 5186.3/T + 0.611*np.log10(T)-6.7497
    K_p_b = np.power(10, (log_K_p))
    return K_p_b


# 理論平衡定数求める用パラメーター・上からSO2,SO3,O2左からH,a,b,c,d
a_p = np.array([[-70944.1, 13.609, 0.270076, -10.6501, 2.07935],
                [-94579.4, 19.3905, 0.200765, -17.5096, 3.27916],
                [0.0, 8.20985, 0.458891, -4.40966, 0.970363]])

params = a_p[1, :]-a_p[0, :]-a_p[2, :]/2
print(params)


def ideal(T):
    t = sp.Symbol("t")
    C_p = params[1]+params[2]*t/1000+params[3] * \
        (10**5)/(t**2)+params[4]*(10**8)/(t**3)
    print(C_p)  # 比熱の式もとめた
    del_H = sp.integrate(C_p, t)
    print(del_H)  # 比熱の式不定積分した
    del_H_ = del_H.subs(t, T)-del_H.subs(t, 298)  # 定積分にした
    _del_H_ = del_H_+params[0]
    # 生成エンタルピーもとめた(負になるはず)
    # 気体定数R=1.99[cal/K*mol]
    del_H_RT = _del_H_/(np.power(t, 2)*1.99)  # 理論平衡定数の式たてた
    ln_K = sp.integrate(del_H_RT, t)
    # 温度代入した(lnK2-lnk1がもとまる、このときlnK1は298ｋでの平衡定数)
    ln_K2_ln_K1 = ln_K.subs(t, T)-ln_K.subs(t, 298)
    ln_K_ = ln_K2_ln_K1+28.57  # ln_K1たした
    K_ideal = sp.exp(ln_K_)  # ln取った
    return K_ideal


# パラメーターとか温度ごとにまとめて配列にする
# 温度、入口SO2濃度,酸素濃度、ガス圧,反応率の順
a_r = np.array([[673, 18.9, 16.95, 0.996, 0.713],
                [773, 20.0, 16.72, 0.998, 0.903],
                [873, 21.6, 16.39, 0.996, 0.740]])


K_p = list(eq(a_r[:, 1], a_r[:, 2], a_r[:, 3], a_r[:, 4]))
print(K_p)  # 普通の(実験値)

ideal = [ideal(673), ideal(773), ideal(873)]
print(ideal)  # 理論平衡定数

K_p_B_P = list(b_and_p(a_r[:, 0]))
print(K_p_B_P)  # Bohdenstin &Pohl

for_plt = np.array([list(eq(a_r[:, 1], a_r[:, 2], a_r[:, 3], a_r[:, 4])),
                    ideal, list(b_and_p(a_r[:, 0])),
                    [1/400, 1/500, 1/600]])
print(for_plt)

T_ = for_plt[3, :]
expe = for_plt[0, :]
B_P = for_plt[2, :]
ideal = for_plt[1, :]


fig = plt.figure(figsize=(6, 6))
plt.title("1/T & equibilium coefficients")
plt.plot(T_, expe, label="experimental value")
plt.plot(T_, B_P, label="value of Bohdenstein&Pohl")
plt.plot(T_, ideal, label="ideal value")
plt.xlabel("1/T")
plt.xlim(0.0015, 0.0028)
plt.ylabel("equibilium coefficients")
plt.legend(loc="upper left")
plt.show()
