#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

####定数たち#####
#添え字　_e:エタノール　_w:水　 _g:気相　  _l:液相
#大気圧を[mmHg]に変換
P = 992*0.75
#各成分のAntoineパラメーター
a_e=[8.11220,1592.864,226.184]
a_w=[8.07131,1730.630,233.426]

#Margulesパラメーター
a=1.6941
b=1.2126
####式の定義#####
#Tの入力でPiを得るAntoine式を定義
def antoine(T,A,B,C):
   a_para=A-B/(T+C)
   Pi_=np.power(10,a_para)
   Pi=np.round(Pi_,decimals=4)
   return Pi

#Margules式で活量係数を求める
def margules(x):
    gamma_1=np.exp((1-x)**2*(a+2*(b-a)*x))
    gamma_2=np.exp(x**2*(b+2*(a-b)*(1-x)))
    return [gamma_1,gamma_2]

#気相組成求める
def gas_comp(gamma,x,Pi):
    y=(gamma*x*Pi)/P
    return y

#各組成における沸点を求める
x=np.arange(0,1.01,0.05)
T=np.arange(76.0,100,0.1)
print(T.size)
print(x.size)
list=[]
for r in range (0,21):
    x_e=x[r]
    x_w=1-x_e
    for t in range (0,240):
        #温度仮定
        T_=T[t]
        #蒸気圧求める
        P_e=antoine(T_,a_e[0],a_e[1],a_e[2])
        P_w=antoine(T_,a_w[0],a_w[1],a_w[2])
        gamma_e=(margules(x_e))[0]
        gamma_w=(margules(x_e))[1]
        #気相組成求める
        y_e=gas_comp(gamma_e,x_e,P_e)
        y_w=gas_comp(gamma_w,x_w,P_w)
        #確認
        if 0.99 < y_e + y_w < 1.01:
            list.append([np.round(x_e,decimals=4),np.round(T_,decimals=4),np.round(y_e,decimals=4)])
            break
        else:
            t = t+1
    r=r+1
print(list)
array=np.asarray(list)


#T-x,y線図
x=array[:,0]
T=array[:,1]
y=array[:,2]

fig=plt.figure(figsize=(12, 6))
fig.suptitle("(T-x,y) & (x-y) curve under 997[hPa]")
ax1=fig.add_subplot(1,2,1)
ax1.scatter(x,T,c="red",label="liquid phese",s=2)
ax1.scatter(y,T,c="blue",label="gas phese",s=2)
ax1.set_title('gas-liquid equibilium curve\n in ethanol-water mixed solution')
ax1.set_xlabel('x1,y1')
ax1.set_ylabel('tempeture')
ax1.legend(loc='upper right')

#x-y線図
ax2=fig.add_subplot(1,2,2)
ax2.scatter(x,y,c="green",s=2)
ax2.set_title('composition curve at equibilium \nin ethanol-water mixed solution ')
ax2.set_xlabel("x:liquid phese")
ax2.set_ylabel("y:gas phese")
plt.show()

#重ねてみ


# %%
