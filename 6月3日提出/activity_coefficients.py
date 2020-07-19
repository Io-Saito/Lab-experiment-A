import numpy as np

#エタノール・水二成分系
####定数たち#####
#大気圧を[mmHg]に変換
P = 992*0.75

#添え字　_e:エタノール　_w:水　 _g:気相　  _l:液相
#各成分のアントワンパラメーター
a_e=[8.11220,1592.864,226.184]
a_w=[8.07131,1730.630,233.426]

###式の定義###
#密度から平衡組成を求める式
def comp(rho):
    x_ = 119.662593*rho - 42.2257684*rho*rho + 38.5195457/rho -115.974295
    x  = np.round(x_,decimals=4)
    return x

#Tの入力でPiを得るAntoine式を定義
def antoine(T,A,B,C):
   a_para=A-B/(T+C)
   Pi_=np.power(10,a_para)
   Pi=np.round(Pi_,decimals=4)
   return Pi

#気相組成計算
def gas_comp(gamma,x,Pi):
    y=(gamma*x*Pi)/P
    return y

#活量係数γ
def activity(P_,l,g):
    gamma_=(P*g)/(P_*l)
    gamma=np.round(gamma_,decimals=4)
    return gamma

#######計算するよ######
#組成
rho_l=0.8998
l_e=comp(rho_l)
rho_g=0.8407
g_e=comp(rho_g)
l_w = 1-l_e
g_w = 1-g_e

#飽和蒸気圧を決めるのは液相温度。
T = 80.4
#純成分系蒸気圧
P_e=antoine(T,a_e[0],a_e[1],a_e[2])
P_w=antoine(T,a_w[0],a_w[1],a_w[2])

#活量係数求める
gamma_e=activity(P_e,l_e,g_e)
gamma_w=activity(P_w,l_w,g_w)
#有効数字
print(gamma_e,gamma_w)

####単位変換してPandasで表を書く####
#圧力[Pa]
P_=992*10**2
#平衡温度[K]＠液相
T_si=T+273
#蒸気圧[Pa]
P_e_=np.round(P_e/0.75,decimals=4)
P_w_=np.round(P_w/0.75,decimals=4)
#活量係数[-]

print(P_,T_si,l_e,g_e,P_e_,P_w_,gamma_e,gamma_w)
