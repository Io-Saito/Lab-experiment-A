# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
# %%
df = pd.read_csv("Book1.csv", header=4, names=[
                 "Pressure", "Temp", "sep1", "sep2", "reactor", "compressor", "yield"], index_col=False)
df

temp_p = 552.34
pres_p = 34.83

# %%
# Xを固定してYを変化させた時のZの変化をみる
# X,Y=温度or圧力
# Zはそのほか
df_pressure = df[df["Temp"] == temp_p]
df_temp = df[df["Pressure"] == pres_p]

# %%
df_pressure
df_temp
# %%
# 圧力変化のグラフ
columns = ["sep1", "sep2", "reactor", "compressor", "yield"]


def graph(p):
    if p == True:
        df_ = df_pressure
        X = "Pressure"
        XX = "温度一定"
        X_label = "圧力"
    else:
        df_ = df_temp
        X = "Temp"
        XX = "圧力一定"
        X_label = "温度"
    for r in columns:
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111)
        ax.scatter(df_[X], df_[r])
        ax.legend(loc="upper right")
        ax.set_xlabel(X_label)
        ax.set_ylabel(r)
        fig.savefig(XX+"_"+r+".png")


# %%
graph(p=False)

# %%
fig1 = plt.figure(figsize=(8, 8))
ax1 = fig1.add_subplot(111)
ax1.scatter(df_pressure["Pressure"], df_pressure["yield"])
ax1.set_xlabel("圧力")
ax1.set_ylabel("収率")
ax1.set_ylim(0, 1)
fig1.savefig("圧力"+"_"+"収率"+".png")

# %%
