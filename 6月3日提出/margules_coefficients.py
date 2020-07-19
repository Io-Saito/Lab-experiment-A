import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

#さっき求めた組成と活量係数からMargles定数を求める
#添え字　_e:エタノール　_w:水　 _g:気相　  _l:液相
#連立方程式の定数を定義。Scipyは神。
A = sp.Symbol("A")
B = sp.Symbol("B")
#組成
l_e=0.3194
l_w=0.6003

#活量係数
gammma_e=1.6941
gam_e=sp.log(gammma_e)
gammma_w=1.2126
gam_w=sp.log(gammma_w)

#Margules式X２を定義。lnはめんどいのでexpで右辺に突っ込む。
eq1= (A+2*(B-A)*l_e)*l_w**2-gam_e
eq2 = (B+2*(A-B)*l_w)*l_e**2-gam_w
#解く。
M_paras=sp.solve([eq1, eq2])
M_=list(M_paras.values())
a = M_[0]
b = M_[1]
print(M_)
#Gibbs-Duhemの式
#グラフ描画(いいかんじ)
x = np.linspace(0,1,100,endpoint=False)
M_1 = np.power((1-x),2)*(a+2*(b-a)*x)
M_2 = np.power(x,2)*(b+2*(a-b)*(1-x))
y = M_1-M_2
fig=plt.figure(figsize=(12, 8))
ax=fig.add_subplot()
ax.plot(x,y)
ax.axhline(y=0,xmax=1,xmin=0,c='black')
plt.show()

#積分してみる(末端の定義どうしよう)
gd=sp.integrate(y,(x))
print(gd)
