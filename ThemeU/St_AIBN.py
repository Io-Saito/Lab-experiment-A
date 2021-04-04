# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats as stats
import japanize_matplotlib
# from matplotlib import rc
# rc('text', usetex=True)
import pytablewriter

# %%
df = pd.DataFrame(np.array([[0.2877, 0.5086, 0.3528, 0.5627, 0.6473, 0.8597, 0.3983, 0.4260, 0.5092, 0.6361, 0.0592, 0.2979, 0.2882, 0.5389, 0.2599, 0.4766],
                            [30.2, 60.3, 51.0, 84.0, 100.5, 149.6, 88.4, 133.5,
                                149.2, 202.0, 21.5, 41.6, 45.0, 70.8, 99.9, 169.9],
                            [15, 15, 10, 10, 10, 10, 5, 5, 5, 5, 15, 15, 10, 10, 5, 5]]).T, columns=["poly", "AIBN", "St"])
display(df)
# %%
df["St_mol"] = df["St_mol"]*100
df["AIBN_mol"] = df["AIBN_mol"]*1000
#%%
writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(df.sort_values("St"))
writer.write_table()

# %%
# スチレンモノマー密度＝0.910[g/ml],式量=104.15
# AIBN分子量=164.21[g/mol]
St_density = 0.910
St_MW = 104.15
AIBN_MW = 164.21
df["St_mol"] = df["St"]*St_density/St_MW
df["AIBN_mol"] = df["AIBN"]/(AIBN_MW*1000)
df["conc"] = df["AIBN_mol"]*100/df["St_mol"]

display(df)

# %%
# df_s = df.sort_values("conc")
# df__s = df_s.drop(df_s.index[0])


def curve(x, a, b):
    y = b*(x**a)
    return y


param_0, cov_0 = curve_fit(curve, df["conc"], df["poly"])


def curve_func(x, param):
    y = param[1]*(x**param[0])
    return y


display(param_0, cov_0)

# %%
# 誤差項＝正規分布を仮定して分散、平均を求める
gosa = np.log(df["poly"])-np.log(curve_func(df["conc"], param_0))


def smirnov_grrubs(array, alpha):
    data = np.array(array)
    kikyaku = []
    while True:
        n = len(data)
        t = stats.t.isf(q=(alpha/(n*2)), df=(n-2))
        # 100α/nパーセンタイル,自由度n-2のt値
        tau = (n-1)*t/(np.sqrt(n*(n-2)+n*t**2))  # τ
        mu, std = np.mean(data), np.std(data, ddof=1)  # 誤差項の平均、分散
        data_far = np.where(np.abs(data-mu) == np.max(np.abs(data-mu)))
        ind = ((data_far[0]).tolist())[0]
        tau_far = np.abs((data[ind]-mu)/std)
        if np.abs(tau_far) < tau:
            display("外れ値なし")
            break
        else:
            display(f'τ:{tau}<外れ値のτ:{tau_far}より棄却')
            display(f'棄却値:{data[ind]}')
            data = np.delete(data, ind, axis=0)
            kikyaku.append(ind)
    return kikyaku


index = smirnov_grrubs(gosa, 0.01)


df_s = df.drop(df.index[index[0]])


param_1, cov_1 = curve_fit(curve, df_s["conc"], df_s["poly"])

lin = np.linspace(0.1, 3.0, 100)
y = curve_func(lin, param_1)


# %%
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(df_s["conc"], df_s["poly"], label="実験値")
ax1.scatter(df["conc"][index[0]], df["poly"]
            [index[0]], color="red", label="除外")
ax1.plot(lin, y, color="orange", label="累乗近似")
ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_title("開始剤濃度とポリマー重合速度の関係")
ax1.set_xlabel("AIBN濃度[mol%]")
ax1.set_ylabel("ポリマー反応速度[g/h]")
ax1.legend(loc="lower right")
fig.show()

# %%
