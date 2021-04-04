# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import os
import sympy as sp
from sympy.matrices.common import a2idx


# %%


def open_file(path_name):
    data = pd.read_csv(
        path_name)
    E = data.values[:, 2]
    I = data.values[:, 3]
    return E, I


# %%
path = "/Users/io/Documents/課題/6semester/実験B/ThemeP/"
file_list = []
files = os.listdir(path)
for file in files:
    base, ext = os.path.splitext(file)
    if ext == '.csv':
        file_list.append({"file": file, "ext": ext})

display(file_list)
# %%

list_csv = []
r = 0
for file in file_list:
    E = open_file(path+file["file"])[0]
    I = open_file(path+file["file"])[1]
    list_csv.append(
        {"Name": file["file"], "E": E, "I": I})


# %%
fig = plt.figure(figsize=(6, 8))
ax1 = fig.add_subplot(111)
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['left'].set_position(('data', 0))
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.plot(list_csv[0]["E"], list_csv[0]["I"], label="FMAのみ")
ax1.plot(list_csv[7]["E"], list_csv[7]["I"], label="グルコース1回目")
ax1.plot(list_csv[6]["E"], list_csv[6]["I"], label="グルコース2回目")
ax1.plot(list_csv[5]["E"], list_csv[5]["I"], label="グルコース3回目")
ax1.plot(list_csv[8]["E"], list_csv[8]["I"], label="グルコース4回目")
ax1.plot(list_csv[8]["E"], list_csv[8]["I"], label="グルコース5回目")

ax1.set_title("E-Iグラフ(溶存酸素計,FMA使用)")
ax1.legend(loc="upper right")

ax1.set_xlabel("電圧[V]")
ax1.set_ylabel("電流[A]")
plt.show()
# %%
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['left'].set_position(('data', 0))
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax2.spines['bottom'].set_position(('data', 0))
ax2.spines['left'].set_position(('data', 0))
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.plot(list_csv[2]["E"], list_csv[2]["I"], label="リン酸緩衝液")
ax1.plot(list_csv[11]["E"], list_csv[11]["I"], label="亜硫酸Na")
ax2.plot(list_csv[3]["E"], list_csv[3]["I"], label="リン酸緩衝液")
ax2.plot(list_csv[4]["E"], list_csv[4]["I"], label="GOD")
ax2.plot(list_csv[10]["E"], list_csv[10]["I"], label="グルコース")

fig.suptitle("E-Iグラフ")
ax1.legend(loc="lower right")
ax2.legend(loc="lower right")
ax1.set_xlabel("電圧[V]")
ax1.set_ylabel("電流[A]")
ax2.set_xlabel("電圧[V]")
ax2.set_ylabel("電流[A]")
ax1.set_title("リン酸緩衝液-亜硫酸Na")
ax2.set_title("グルコース、GODによる還元電流の検出")
plt.show()
# %%
# リン酸緩衝液体積[mL]
PBS = 100
# グルコース添加量[ml]
G_in = np.array([0, 100, 200, 300, 400, 500])/1000
# グルコース濃度[mol/mL]
conc = 0.1/1000
# 溶存酸素
O2 = np.array([3.4, 3.3, 3.1, 2.9, 2.6, 2.3])
# グルコース濃度[M]
conc_G = G_in*conc/100*1000
x_lin = np.linspace(0.0, 3.5, 50)
Calibration = np.polyfit(O2, conc_G, 1)
curve = np.poly1d(Calibration)(x_lin)


Unknown = np.poly1d(Calibration)(2.7)
display(Calibration)
# 溶液に対するグルコース濃度
Unknown_2 = Unknown*(100+0.4)/0.1
display(Unknown_2)
# %%
fig = plt.figure(figsize=(6, 6))
ax1 = fig.add_subplot(111)
ax1.scatter(O2, conc_G, label="測定結果")
ax1.plot(x_lin, curve, label="検量線")
ax1.set_title("検量線")
ax1.legend(loc="upper right")
ax1.set_xlabel("溶存酸素[mg/L]")
ax1.set_ylabel("溶液中のグルコース濃度")
plt.show()

# %%
