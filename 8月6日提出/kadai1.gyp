# %%
import matplotlib.pyplot as plt
import numpy as np

# ヘンリー定数
# 飽和CO2濃度
# 液膜Re数
# 膜厚

# ヘンリー定数(単位：MPa)


def henry(t):
    ln_Kh = 29.319*(1-298.15/t)-21.669*np.log(t/298.15)+0.3287*(t/298.15-1)
    Kh = np.exp(ln_Kh)*165.8
    return Kh


# 温度：17.6度
H = henry(17.6+273.15)
display(H)
pA = 0.1013
x_A = pA/H
display(x_A)
# モル密度を求める
M = 998.67*1000/18.2

# 飽和濃度[mol/m^3]
CA = M*x_A
display(CA)


# %%
