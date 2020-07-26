# %%
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.optimize import curve_fit
import pandas as pd
import pytablewriter
# %%
m = np.array([13, 17, 20, 23, 29, 30.50, 43])
bp = np.array([23130, 9416, 6557, 4361, 2332, 2027, 564])
bp_log = np.log10(bp[1:6])
m_lin = m[1:6]
display(bp_log)
lin = np.linspace(10, 45, 200)
poly = np.polyfit(m_lin, bp_log, 1)
display(poly)


def func2(x, a, b):
    return a*x+b


popt2, pcov2 = curve_fit(func2, m_lin, bp_log)
print(popt2)
linear2 = popt2[0]*lin+popt2[1]
linear = 10**(np.poly1d(poly)(lin))
# %%
x = np.poly1d(poly)(34)
display(x)
display(10**x)
# %%
fig = plt.figure(figsize=(18, 6))
ax1 = fig.add_subplot(1, 2, 1)
# ax2 = ax1.twinx()
ax1.scatter(m, bp, label="experimental value")
ax1.plot(lin, linear, label="linear approximation")
ax1.set_yscale('log')
ax1.set_title("mobility VS polymerization Semilog graph")
ax1.set_xlabel("mobility[mm]")
ax1.set_ylabel("polymerization[bp] at log scale")
ax1.legend(loc="upper right")
plt.show()


# %%
table = np.transpose(
    np.vstack((m, bp)))
display(table)
column = ["移動度[㎜]", "重合度[bp]"]
df = pd.DataFrame(data=table, columns=column)
display(df)
writer = pytablewriter.MarkdownTableWriter()

writer.from_dataframe(df)
hoge = str(writer.write_table())
print(hoge)

# %%
ppc.copy(hoge)


# %%
