# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%
# Tbのデータを読み込み
CaS_Tb_df = pd.read_csv("CaS_Tb_F.csv", header=7)
KCl_Tb_df = pd.read_csv("KCl_Tb_F.csv", header=7)
display(KCl_Tb_df)

# %%
CaS_Tb_arr = CaS_Tb_df.values[:, 0:2]
KCl_Tb_arr = KCl_Tb_df.values[:, 0:2]

CaS_length = CaS_Tb_arr[:, 0]
CaS_spectol = CaS_Tb_arr[:, 1]
KCl_length = KCl_Tb_arr[:, 0]
KCl_spectol = KCl_Tb_arr[:, 1]

# %%
fig = plt.figure(figsize=(18, 6))
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(CaS_length, CaS_spectol, label="CaS")
ax1.plot(KCl_length, KCl_spectol, label="KCl")
ax1.set_title("Fluorescence spectrum -Tb")
ax1.set_xlabel("length[nm]")
ax1.set_ylabel("strength[arb]")
ax1.set_xlim(350, 600)
ax1.legend()
plt.show()


# %%
