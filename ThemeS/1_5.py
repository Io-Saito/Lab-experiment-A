# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import japanize_matplotlib
import sklearn.metrics as metrics

# %%
df_15 = pd.read_csv(
    "/Users/io/Documents/課題/6semester/実験B/ThemeS/CSV/1_5_2.csv", header=1)

# %%
df_15
# %%
df_15 = df_15.dropna(how="all", axis=1)
df_15.columns = ["200_E", "200_I", "100_E",
                 "100_I", "50_E", "50_I", "20_E", "20_I"]

# %%
names = df_15.columns
labels = ["200[mV/s]", "100[mV/s]", "50[mV/s]", "20[mV/s]"]
display(names)
# %%
fig2 = plt.figure(figsize=(8, 8))
ax2 = fig2.add_subplot(111)
for i in range(0, 8, 2):
    ax2.plot(df_15[names[i]], df_15[names[i+1]], label=labels[int(i/2)])
    i = i+1
# ax2.scatter(peekE_min, peek_min, color="black")
# ax2.scatter(peekE_max, peek_max, color="black")
# ax2.legend()
ax2.spines['bottom'].set_position(('data', 0))
ax2.set_ylabel("電流")
ax2.set_xlabel("電圧")
ax2.set_title("白金電極を用いた水の電気分解の電流-電圧特性")
fig2.show()
fig2.savefig("15_1")

# %%
# 水素吸着ピークの取得
# ピーク検出
peek_max = []
index_max = []
for i in range(0, 8, 2):
    # peek_min.append(df_15[names[i+1]].min())
    # index_min.append(df_15[names[i+1]].idxmin())
    peek_max.append(df_15[names[i+1]].max())
    index_max.append(df_15[names[i+1]].idxmax())
    i = i+1

# for i in range(0, 8, 2):
#     df_15[names[i+1]].sort_values
#     i = i+1
# df_15

# %%
df_15["200_I"].sort_values().head(30)
# %%

display(peek_max)
# %%
peekE_min = []
peekE_max = []

# for i, j in enumerate(index_min):
#     display(names[i*2])
#     peek_E = df_15[names[i*2]][j]
#     peekE_min.append(peek_E)

for i, j in enumerate(index_max):
    display(names[i*2])
    peek_E = df_15[names[i*2]][j]
    peekE_max.append(peek_E)
# %%
display(peekE_max)
# display(peekE_min)
v = np.array([200, 100, 50, 20])
# %%

peekE_min = np.array([-0.165, -0.143, -0.127, -0.122])
peek_min = np.array([-0.003, -0.0016, -0.00088, -0.00043])
# %%
display(peek_max)
# %%
lin = np.linspace(0, 200, 1000)
poly_min = np.polyfit(v, peek_min, 1)
poly_max = np.polyfit(v, peek_max, 1)
r2_min = metrics.r2_score(peek_min, np.poly1d(poly_min)(v))
r2_max = metrics.r2_score(peek_max, np.poly1d(poly_max)(v))
line_min = np.poly1d(poly_min)(lin)
line_max = np.poly1d(poly_max)(lin)
display(r2_min, r2_max)
# %%

fig3 = plt.figure(figsize=(8, 8))
ax3 = fig3.add_subplot(111)
ax4 = ax3.twinx()
ax3.scatter(v, peek_min, label="実験値(還元電流)")
ax4.scatter(v, peek_max, label="実験値(酸化電流)", color="orange")
ax3.plot(lin, line_min, label="最小二乗近似(R二乗=0.99984)")
ax4.plot(lin, line_max, label="最小二乗近似(R二乗=0.99967)", color="orange")
ax3.legend(loc="upper center")
ax4.legend(loc="lower center")
ax3.set_xlabel("掃引速度")
ax3.set_ylabel("ピーク還元電流(水素吸着)")
ax4.set_ylabel("ピーク酸化電流(水素脱離)")
ax3.set_title("ピーク電流と掃引速度の関係")
fig3.savefig("ピーク電流と掃引速度の関係(白金)")
fig3.show()


# %%
