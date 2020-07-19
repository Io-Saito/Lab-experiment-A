# %%
import numpy as np
import pytablewriter
import pandas as pd

# %%
# ほしい溶液の濃度[mM]
conc = np.array([0.3, 0.6, 0.9, 1.2, 1.5])
# 1Lあたりの物質量[mol]
conc_L = conc/1000
# １Lあたりの質量[g]
conc_M = conc_L*178.23
# 10mLあたりの質量[g]
conc_tenmL = conc_M/100
# ↑は、作った20ｍLの溶液のうち１mLに含まれていた質量。[g]
conc_twenty = np.round(conc_tenmL*20*1000, 3)

display(conc_twenty)

# %%
# 20mLいきなり作る
conc__twenty = np.round(conc_M/50*1000, 4)
display(conc__twenty)

conc_real = np.array([0.289, 0.573, 0.856, 1.167, 1.461])

# %%
table = np.transpose(np.vstack((conc, conc_twenty, conc__twenty, conc_real)))
display(table)
# %%
columns = ["目標濃度", "10倍希釈するとき", "10倍希釈しないとき", "実際の濃度"]
df = pd.DataFrame(data=table, columns=columns)
print(df)

writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(df)
writer.write_table()


# %%
