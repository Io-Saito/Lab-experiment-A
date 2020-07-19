# %%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pytablewriter
import scipy as sp
from scipy.interpolate import lagrange
# %%
data = pd.read_csv("b_n_n.csv", header=None)
# 質量分率求める
# phenole　4.5888g
# 水密度＠25℃　0.998g/ml
for_plt = []
phe = 4.5888
water = 0.998
arr = data.values
fp_2 = np.mean([arr[0, 2], arr[1, 2], arr[2, 2], arr[3, 2]])
conc_2 = np.divide(phe, (arr[0, 0]*water)+phe)
list_plt = [[fp_2, conc_2]]

r = 0
while r < 9:
    fp_r = np.mean([arr[4+r*3, 2], arr[5+r*3, 2], arr[6+r*3, 2]])
    conc_r = np.divide(phe, (arr[4+3*r, 0]*water)+phe)
    list_r = [fp_r, conc_r]
    list_plt.append(list_r)
    r = r+1

list_for_plt = np.array(list_plt)

x = list_for_plt[:, 1]
y = list_for_plt[:, 0]

x_lin = np.linspace(0.1, 0.7, 1000)
lag = lagrange(x, y)
display(list_for_plt)
lag_plt = np.poly1d(lag)(x_lin)


def tie(z):
    lag_ = np.array(lag)
    var = lag_[9]-z
    display(var)
    np.put(lag_, 9, var)
    return np.roots(lag_)


# タイライン
z = [55, 58, 60, 62, 65]
r = 0
while r < 5:
    display(tie(z[r]))
    r = r+1

low = np.array([0.143, 0.161, 0.179, 0.204, 0.276])
high = np.array([0.608, 0.592, 0.574, 0.532, 0.449])
zz = np.array(z)

ave = (low+high)/2
display(ave)

table = np.transpose(np.vstack(
    (zz, low, high, ave)))
columns = ["温度", "低フェノール組成", "高フェノール組成", "予想されるUCST組成"]
df = pd.DataFrame(data=table, columns=columns)

# %%
writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(df)
writer.write_table()
# 平均
# %%
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax1.scatter(x, y, label="experimental value")
ax1.plot(x, y, label="experimental line")
ax1.plot(x_lin, lag_plt, label="approximation on lagrange interpolation ")
ax1.scatter(low, zz, color="red", label="tieline")
ax1.scatter(high, zz, color="red")
ax1.set_title("water&phenole Mutual dissolution")
ax1.set_xlabel("phenole mass fraction[-]")
ax1.set_ylabel("dissolve temperature[℃]")
r = 0
while r < 5:
    ax1.hlines(y=zz[r], xmin=low[r], xmax=high[r],
               color="red")
    r = r+1
ax1.scatter(ave, zz, label="UCST", color="green")
ax1.grid()
ax1.legend(loc="downer center")
plt.show()
# %%


# %%
