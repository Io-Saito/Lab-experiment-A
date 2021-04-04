# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import japanize_matplotlib
import sklearn.metrics as metrics
# %%
df_14A = pd.read_csv("/Users/io/Documents/課題/6semester/実験B/ThemeS/CSV/1_4A.csv", header=1,
                     names=["10_E", "10_I", "0", "20_E", "20_I", "1", "50_E", "50_I", "2", "100_E", "100_I"])
# %%
df_14A = df_14A.dropna(how="all", axis=1)
# %%
df_14A
names = df_14A.columns
labels = ["10[mV/s]", "20[mV/s]", "50[mV/s]", "100[mV/s]"]
display(names)
# %%
fig1 = plt.figure(figsize=(6, 6))
ax1 = fig1.add_subplot(111)
for i in range(0, 8, 2):
    ax1.plot(df_14A[names[i]], df_14A[names[i+1]], label=labels[int(i/2)])
    i = i+1
ax1.legend()
ax1.set_ylabel("電流[A]")
ax1.set_xlabel("電圧[E]")
ax1.spines['bottom'].set_position(('data', 0))
ax1.set_title("RC回路の電流-電圧特性")
fig1.show()
fig1.savefig("14A")
# %%


def capa(num):
    col = str(num)+"_I"
    n = int(len(df_14A[col].dropna().index)/2)
    display(df_14A[col].head(n).mean())
    cap = df_14A[col].head(n).mean()/num
    return cap


# %%
data = [10, 20, 50, 100]
for r in data:
    display(capa(r))
# %%
df_14B = pd.read_csv(
    "/Users/io/Documents/課題/6semester/実験B/ThemeS/CSV/1_4B.csv", header=1, names=["5_E", "5_I", "6", "10_E", "10_I", "0", "20_E", "20_I", "1", "50_E", "50_I", "2", "100_E", "100_I", "3", "200_E", "200_I"])

# %%

df_14B = df_14B.dropna(how="all", axis=1)
# %%
df_14B

# %%
names = df_14B.columns
labels = ["5[mV/s]", "10[mV/s]", "20[mV/s]",
          "50[mV/s]", "100[mV/s]", "200[mV/s]"]
display(names)
# %%
fig2 = plt.figure(figsize=(6, 6))
ax2 = fig2.add_subplot(111)
for i in range(0, 12, 2):
    ax2.plot(df_14B[names[i]], df_14B[names[i+1]], label=labels[int(i/2)])
    i = i+1
ax2.spines['bottom'].set_position(('data', 0))
ax2.legend()
ax2.set_ylabel("電流[A]")
ax2.set_xlabel("電圧[V]")
ax2.set_title("酸化還元反応の電流-電圧特性")
fig2.show()
fig2.savefig("14B_1")


# %%
# ピーク検出
peek = []
index = []
for i in range(0, 12, 2):
    peek.append(df_14B[names[i+1]].max())
    index.append(df_14B[names[i+1]].idxmax())
    i = i+1
# %%
# ピークvs走査速度
v = np.array([5, 10, 20, 50, 100, 200])
fig3 = plt.figure(figsize=(6, 6))
ax3 = fig3.add_subplot(111)
ax3.scatter(np.sqrt(v), peek, label="実験値")
ax3.plot(lin, line, label="最小二乗近似(R^2=0.9997)")
ax3.legend(loc="upper left")
ax3.set_xlabel("掃引速度の平方根[(mV/s)^1/2]")
ax3.set_ylabel("ピーク電流[A]")
ax3.set_title("ピーク電流と掃引速度の関係")
fig3.savefig("ピーク電流と掃引速度の関係")
fig3.show()

# %%
# ピーク電位vs走査速度
v = np.array([5, 10, 20, 50, 100, 200])
fig4 = plt.figure(figsize=(6, 6))
ax4 = fig4.add_subplot(111)
ax4.scatter(v, peekE, label="実験値")
ax4.legend(loc="upper left")
ax4.set_xlabel("掃引速度[mV/s]")
ax4.set_ylabel("ピーク電圧[V]")
ax4.set_ylim(-0.3, 0.9)
ax4.set_title("ピーク電圧と掃引速度の関係")
fig4.savefig("ピーク電圧と掃引速度の関係")
fig4.show()

# %%
lin = np.linspace(0, 15, 150)
poly = np.polyfit(np.sqrt(v), peek, 1)
display(poly)
line = np.poly1d(poly)(lin)
r2 = metrics.r2_score(peek, np.poly1d(poly)(np.sqrt(v)))
display(r2)
# %%


# %%

# ピーク電圧を求める
# peek[0]->5
# peek[1]->10
# columnsのi*2番目から探索すればOK
peekE = []
for i, j in enumerate(index):
    display(names[i*2])
    peek_E = df_14B[names[i*2]][j]
    peekE.append(peek_E)
# %%
peekE
# %%
