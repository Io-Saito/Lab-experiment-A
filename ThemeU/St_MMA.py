# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy.stats as stats
import japanize_matplotlib
import matplotlib as mpl
from matplotlib import rc
import pytablewriter
rc('text', usetex=True)
print(mpl.get_configdir())
print(mpl.matplotlib_fname())
# %%
df = pd.DataFrame(np.array([[10, 8, 6, 4, 2, 11, 7, 5], [2, 4, 6, 8, 10, 1, 5, 7], [
                  5.53, 8.14, 11.31, 16.83, 30.06, 4.29, 9.96, 13.53]]).T, columns=["St", "MMA", "integral"])

# %%
display(df)

# %%
MMA_MW = 100.12
MMA_density = 0.944
St_density = 0.910
St_MW = 104.15

# %%
# St/MMAで考えてる
df["shikomi"] = (df["St"]*St_density/St_MW)/(df["MMA"]*MMA_density/MMA_MW)
df["polymer"] = (8/(df["integral"]+5))/(1-(8/(df["integral"]+5)))
x = np.array(df["shikomi"]**2/df["polymer"])
y = np.array(df["shikomi"] * (df["polymer"]-1)/df["polymer"])
display(x)
display(df)
lin = np.linspace(0, 20, 100)
poly = np.polyfit(x, y, 1)
line = np.poly1d(poly)(lin)
display(poly)
poly2 = np.poly1d([0.52, -0.46])
line2 = np.poly1d(poly2)(lin)
writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(df)
writer.write_table()
# %%
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(x, y, label="experimental")
ax1.plot(lin, line, color="orange", label="approximation")
ax1.plot(lin, line2, color="red", label="theoretical")
ax1.legend(loc="upper left")
ax1.set_title("Finemann-Ross plot")
ax1.set_xlabel(r"$\frac{F^2}{f}$")
ax1.set_ylabel(r"$\frac{F(f-1)}{f}$")
fig.show()
