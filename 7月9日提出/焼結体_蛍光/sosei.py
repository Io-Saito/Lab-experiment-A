# %%
import numpy as np
import pytablewriter
import pandas as pd
# %%
# 総質量　0.005[g]
# モル比　ホスト：ドーパント=1：0.005

# ホスト・ドーパントそれぞれの分子量から質量比をだす


def hoge(h, d):
    h_ = h
    d_ = d*0.005
    t = h_+d_
    k = 0.005/t
    host = np.round(k*h_*1000, 3)
    dopant = np.round(k*d_*1000, 3)
    arr = np.array([host, dopant])
    return arr


KCl = 74.55
CaS = 72.14
H2O = 18

KCl_Tb = hoge(KCl, 747.7/4)
KCl_Eu = hoge(KCl, 366.41-6*H2O)
CaS_Eu = hoge(CaS, 366.41-6*H2O)
CaS_Tb = hoge(CaS, 373.38-6*H2O)
# %%
table = np.stack((KCl_Tb, KCl_Eu, CaS_Tb, CaS_Eu))
display(table)

# %%
columns = ["ホスト[mg]", "ドーパント[mg]"]
df = pd.DataFrame(data=table, columns=columns)

writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(df)
writer.write_table()


# %%
