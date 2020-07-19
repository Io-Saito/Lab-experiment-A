# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytablewriter
# %%
# 励起スペクトル
E_df = pd.read_csv("Anthracene_E.csv", header=2)
#　蛍光スペクトル
F_df = pd.read_csv("Anthracene_F.csv", header=2)
# 0.573
C_0573_df = pd.read_csv("0.573 mM.csv", header=None, names=['波長', '強度'])
# 蛍光スペクトル
F_df = pd.read_csv("Anthracene_F.csv", header=2)
# 0.856
C_0856_df = pd.read_csv("0.856 mM.csv", header=None, names=['波長', '強度'])
# 1.167
C_1167_df = pd.read_csv("1.167 mM.csv", header=None, names=['波長', '強度'])
# 1.461
C_1461_df = pd.read_csv("1.461 mM.csv", header=None, names=['波長', '強度'])

C_0289_df = pd.read_csv("0.289ｍM.csv",
                        header=None, names=['波長', '強度'])
# %%
E_arr = E_df.values
C_0573 = C_0573_df.values
C_1461 = C_1461_df.values
C_1167 = C_1167_df.values
C_0856 = C_0856_df.values
C_0289 = C_0289_df.values
F_arr = F_df.values

index = [E_arr, C_0573, C_1461, C_1167, C_0856, F_arr, C_0289]
r = 0
list = []
while r < 7:
    r_x = (index[r])[:, 0]
    r_y = (index[r])[:, 1]
    list.append(r_x)
    list.append(r_y)
    r = r+1


# %%
fig = plt.figure(figsize=(18, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = ax1.twinx()
ax1.plot(list[0], list[1], label="Excitation spectrum")
ax2.plot(list[2], list[3], label="Absoruption spectrum", color="red")
ax1.set_title("Anthracene Excitation vs Absorption at 0.573mM")
ax1.set_xlabel("length[nm]")
ax1.set_ylabel("strength[arb]")
ax2.set_ylabel("Absorbance")
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1+h2, l1+l2, loc='upper right')
plt.show()


# %%
fig = plt.figure(figsize=(18, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(list[10], list[11], label="Excitation spectrum")

ax1.set_title("Anthracene Fluoresence spectrum")
ax1.set_xlabel("length[nm]")
ax1.set_ylabel("strength[arb]")
ax1.legend()
plt.show()


# %%
fig = plt.figure(figsize=(18, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(list[2], list[3], label="0.573")
ax1.plot(list[4], list[5], label="1.461")
ax1.plot(list[6], list[7], label="1.167")
ax1.plot(list[8], list[9], label="0.856")
ax1.plot(list[12], list[13], label="0.289")
ax1.set_title("Anthracene Absorption spectrum")
ax1.set_xlabel("length[nm]")
ax1.set_ylabel("strength[arb]")
ax1.legend()
plt.show()

# %%
display(poly)
# %%
x = [0.573, 0.856, 1.167, 1.461, 0.289]
y = [0.4908, 0.75186, 0.99089, 1.22171, 0.24248]
x_lin = np.linspace(0, 1.5, 1500)
poly = np.polyfit(x, y, 1)
linear = np.poly1d(poly)(x_lin)


fig = plt.figure(figsize=(18, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax1.scatter(x, y, label="Absoruption spectrum")
ax1.plot(x_lin, linear, label="y=0.836x + 0.0126")
ax1.set_title("Molar extinction coefficient ")
ax1.set_xlabel("concentratiom[mM]")
ax1.set_ylabel("strength[arb]")
ax1.legend()
plt.show()


# %%
display(poly)


# %%
# | 番号 | 蛍光波長(短波長から) | 強度 | 吸収波長(長波長から) | 吸光度 |
# |------ | ---------------------- | -------- | ---------------------- | --------|
# | 1 | 393 | 106.4 | 376 | 1.15 |
# | 2 | 404.2 | 506.70 | 357 | 1.22 |
# | 3 | 427 | 360.30 | 340 | 0.85 |
# | 4 | 452 | 110 | 324 | 0.45 |
# 吸収波長[nm]
abso = np.array([376, 357, 340, 324])
floro = np.array([393, 404.2, 427, 452])
# 吸収波長[m]
abso_m = abso/10**9

# 蛍光波長[m]
floro_m = floro/10**9
# エネルギー[J]
# の前にプランク定数
h = 6.626/10**34
c = 2.998*10**9

E = h*c/abso_m
F_E = h*c/floro_m
display(E)


# %%
eV = 1.60218/10**19
EeV = E/eV
FeV = F_E/eV
display(FeV)
display(EeV)
arr1 = np.array([FeV[0]-FeV[1], FeV[1]-FeV[2], FeV[2]-FeV[3]])
arr2 = np.array([EeV[0]-EeV[1], EeV[1]-EeV[2], EeV[2]-EeV[3]])
display(arr1, arr2)

# %%
num = np.array([1, 2, 3, 4])
table = np.transpose(
    np.vstack((num, abso, E*10**18, EeV, floro, F_E*10**18, FeV)))
display(table)
# %%
columns = ["番号", "吸収波長", "光子エネルギー[10^-18 J]",
           "光子エネルギー[eV]", "励起スペクトル", "励起光エネルギー", "励起光エネルギー[eV]"]
df = pd.DataFrame(data=table, columns=columns)
print(df)

writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(df)
writer.write_table()


# %%
table2 = np.transpose(
    np.vstack((arr1, -arr2)))
display(table2)

# %%]
columns = ["吸収エネルギー差", "蛍光エネルギー差"]
df = pd.DataFrame(data=table2, columns=columns)
print(df)

writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(df)
writer.write_table()


# %%
