# %%
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
from scipy.optimize import curve_fit
# %%
df_13 = pd.read_csv("/Users/io/Documents/課題/6semester/実験B/ThemeS/CSV/1_3.csv",
                    names=['name', 'conc', 'temp', 'kappa', '5', '6', '7'], header=0)
# %%

df_13
# %%
water = float(df_13.at[0, "kappa"])
# %%
water

# %%
df_13["kappa"] = df_13["kappa"].astype(float) - water
df_13["conc"] = df_13["conc"].astype(float)
# %%
df_13
# %%
NaCl = df_13.loc[1:7, ["conc", "kappa"]].astype(float)
HCl = df_13.loc[8:14, ["conc", "kappa"]].astype(float)
CH3COOH = df_13.loc[15:21, ["conc", "kappa"]].astype(float)
# %%


def mol_EC(data):
    data["mol_EC"] = 1000*data["kappa"]/data["conc"]
    return data


def kinzi(data):
    lin = np.linspace(0, 0.01, 100)
    data2 = pd.DataFrame()
    data2["lin"] = lin
    poly = np.polyfit(data["conc"], data["kappa"], 1)
    data2["line"] = np.poly1d(poly)(lin)
    return data2, poly


def sqrt_conc(data):
    data["conc_sqrt"] = np.sqrt(data["conc"])
    return data


def Debye_Huckel(C, Y0, A):
    Y = Y0-A*C
    return Y


def mol_EC_inf(data):
    data3 = pd.DataFrame()
    lin = np.linspace(0, 0.35, 350)
    popt, pcov = curve_fit(
        Debye_Huckel, data["conc_sqrt"], data["mol_EC"])
    data3["mol_EC_sqrt"] = Debye_Huckel(lin, popt[0], popt[1])
    data3["lin"] = lin
    residuals = data["mol_EC"] - \
        Debye_Huckel(data["conc_sqrt"], popt[0], popt[1])
    rss = np.sum(residuals**2)  # residual sum of squares = rss
    # total sum of squares = tss
    tss = np.sum((data["mol_EC"]-np.mean(data["mol_EC"]))**2)
    r_squared = 1 - (rss / tss)
    print(f"切片:{popt[0]},傾き:{popt[1]},r^2:{r_squared}")
    return data3, r_squared


# %%
data = [NaCl, HCl, CH3COOH]
d2 = []
d3 = []
for d in data:
    display(d)
    mol_EC(d)
    d2.append(kinzi(d)[0])
    sqrt_conc(d)
    d3.append(mol_EC_inf(d)[0])
    display(mol_EC_inf(d)[0])
# %%
CH3COOH["Kairido"] = CH3COOH["mol_EC"]/(3.965*(10**4))
# %%
CH3COOH["K"] = (CH3COOH["Kairido"]**2)*CH3COOH["conc"]/(1-CH3COOH["Kairido"])

# %%
CH3COOH
# %%
for d in data:
    display(mol_EC_inf(d)[1])
#
# %%
labels = ["NaCl", "HCl", "酢酸"]
fig2 = plt.figure(figsize=(6, 6))
ax2 = fig2.add_subplot(111)
for i, d in enumerate(data):
    ax2.scatter(d["conc_sqrt"], d["mol_EC"], label=labels[i])
for i, d in enumerate(d3):
    ax2.plot(d["lin"], d["mol_EC_sqrt"], label=labels[i]+"(近似)")

ax2.set_xlabel("濃度の平方根")
ax2.set_ylabel("モル導電率")
ax2.legend(loc="upper right")
ax2.set_title("濃度の平方根とモル導電率の関係")
fig2.show()
fig2.savefig("1_3_極限モル伝導率")

# %%
fig1 = plt.figure(figsize=(6, 6))
ax1 = fig1.add_subplot(111)
for i, d in enumerate(data):
    ax1.scatter(d["conc"], d["mol_EC"], label=labels[i])
# for i, d in enumerate(d2):
#     ax1.plot(d["lin"], d["line"], label=labels[i]+"(近似)")

ax1.set_xlabel("濃度")
ax1.set_ylabel("電気伝導率")
ax1.legend(loc="upper right")
ax1.set_title("濃度と伝導率の関係")
fig1.show()
fig1.savefig("1_3_モル伝導率")

# %%
fig3 = plt.figure(figsize=(6, 6))
ax3 = fig3.add_subplot(111)
ax3.scatter(CH3COOH["conc"], CH3COOH["Kairido"])
ax3.set_xlabel("酢酸濃度")
ax3.set_ylabel("解離度")
ax3.legend(loc="upper right")
ax3.set_title("酢酸濃度と解離度の関係")
fig3.show()
fig3.savefig("1_3_解離度")

# %%
fig3 = plt.figure(figsize=(6, 6))
ax3 = fig3.add_subplot(111)
ax3.scatter(CH3COOH["conc"], CH3COOH["Kairido"])
ax3.set_xlabel("酢酸濃度")
ax3.set_ylabel("解離度")
ax3.set_title("酢酸濃度と解離度の関係")
fig3.show()
fig3.savefig("1_3_解離度")

fig4 = plt.figure(figsize=(6, 6))
ax4 = fig4.add_subplot(111)
ax4.scatter(CH3COOH["conc"], CH3COOH["K"])
ax4.set_xlabel("酢酸濃度")
ax4.set_ylabel("平衡定数")
ax4.set_title("酢酸濃度と解離度の関係")
fig4.show()
fig4.savefig("1_3_平衡定数")

# %%
