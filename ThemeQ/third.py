# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
# 課題1：蒸気凝縮速度

g_s = np.array([0.06102, 0.2388])  # 凝縮速度[g/s]
h = 2257  # 蒸発潜熱
Q_s = g_s/1000*h
display(Q_s)

# %%
