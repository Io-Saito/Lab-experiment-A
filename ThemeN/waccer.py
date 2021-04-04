# %%
import numpy as np
# %%

# プロパノール[g](二桁)
P = 12.6120-12.6076
# アセトアルデヒド[g](二桁✖️５けた✖️４けた)✖️３けた
A = P*(36596/8810)*5.74
# アセトアルデヒドの式量
Ace = 44.05
# Pd使用量[mol]
Pd = 0.1002/177.33
display((A/Ace)/Pd)  # 転化率
display(A)
display(A/Ace)
display(Pd)

# %%
ethlene = np.average(np.array(
    [42.07, 24.43, 40.57, 38.86, 40.38, 40.13, 40.27, 40.51, 39.34, 42.34, 38.05, 39.27, 36.00]))
display(ethlene)
# %%
