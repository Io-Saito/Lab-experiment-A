# %%
import numpy as np
import scipy as cp
import sympy as sp
from sympy import oo
import math
import matplotlib.pyplot as plt
# %%


def E_N_for_graph(t, N):
    E = (N**N/math.factorial(N-1))*theta**(N-1)*np.exp(-1*N*theta)
    return E


def E_N(theta, N):
    E = (N**N/math.factorial(N-1))*theta**(N-1)*sp.exp(-1*N*theta)
    return E


def x_A(k, tau, N):
    t = sp.Symbol('t')
    abc = sp.exp(-1*k*tau*t)*E_N(t, N)*E_N(t, N)
    x_a = 1-sp.integrate(abc, (t, 0, 10000000000))
    return x_a


k = 1.59/10000
NN = np.array([1, 3, 5, 10])
theta = np.linspace(0, 5, 1000)
for n in NN:
    display(x_A(k, 260, n))


list = []
for k in NN:
    array = E_N_for_graph(theta, k)
    list.append(array)


# %%
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(theta, list[0], label="N=1")
ax1.plot(theta, list[1], label="N=3")
ax1.plot(theta, list[2], label="N=5")
ax1.plot(theta, list[3], label="N=10")
ax1.legend(loc="upper right")
ax1.set_ylabel("E_theta")
ax1.set_xlabel("theta")
ax1.set_title("theta-E_theta plot")
fig.show()
# %%


def micro_1(kt):
    x_a = kt/(1+kt)
    return x_a


def macro_func():
    the = sp.Symbol('θ')
    n = sp.Symbol('n')
    abc = sp.exp(-1*n*the)*sp.exp(-1*the)
    x_a = 1-sp.integrate(abc, (the, 0, oo))
    return x_a


f = macro_func()
display(f)
display(f.subs([(n, 5)]))
# %%


def macro_1(kt):
    x_a = 1-(1/(kt+1))
    return x_a


display(macro_1(5))
# %%


def micro_2(kt):
    x_a = (1+(1/(2*kt))) - np.sqrt((1+(1/(2*kt)))**2-1)
    return x_a


small = [-0.57721, 0.99999, -0.24991, 0.05519, -0.00976, 0.00107]


large = [2.334733, 0.250621, 3.330657, 1.681534]


def E1_small(x):
    y = small[0]+small[1]*x+small[2] * \
        (x**2)+small[3]*(x**3)+small[4]*(x**4)+small[5]*(x**5)-np.log(x)
    return y


def E_1_large(x):
    y = ((x**2+large[0]*x+large[1]) /
         (x**2+large[2]*x+large[3]))*((np.exp(-1*x))/x)
    return y


def macro_2(kt):
    al = 1/kt
    if 0 < al <= 1:
        x_a = 1-al*np.exp(al)*E1_small(al)
    else:
        x_a = 1-(al*np.exp(al)*E_1_large(al))
    return x_a


kt = np.linspace(0.001, 8, 100)

vfunc = np.vectorize(macro_1)

li = []
for n in kt:
    li.append(macro_2(n))

# %%

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(kt, micro_1(kt), label="micro,n=1")
ax1.plot(kt, macro_1(kt), label="macro,n=1")
ax1.plot(kt, micro_2(kt), label="micro,n=2")
ax1.plot(kt, li, label="macro,n=2")
ax1.legend(loc="lower right")
ax1.set_ylabel("x_A")
ax1.set_xlabel("kτ")
ax1.set_title("difference of reaction rate")
fig.show()

# %%
