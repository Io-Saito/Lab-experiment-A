# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
# 時間、（水）ベンゼン、エチルベンゼン、o-,p-,m-の順番
# t=10
t_0 = np.array([0, 100, 0, 0, 0])
t_10 = np.array([1885/6, 3574081/8, 1018/10, 1719/10, 0])
t_30 = np.array([9551/6, 3412328/8, 11730/10, 18257/10, 0])
t_60 = np.array([102956/6, 3286356/8, 71813/10, 86781/10, 1187/10])

# 面積比
t_area_10 = (t_10/np.sum(t_10))*100
t_area_30 = (t_30/np.sum(t_30))*100
t_area_60 = (t_60/np.sum(t_60))*100
np.set_printoptions(suppress=True)
display(t_area_10, t_area_30, t_area_60)

# %%
table = np.stack([t_0, t_area_10, t_area_30, t_area_60])
display(table)

# %%
t = np.array([0, 10, 30, 60])
# %%
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
ax1.plot(t, table[:, 0], label="benzene")
ax2.plot(t, table[:, 1], label="etyle benzene", color="purple")
ax1.plot(t, table[:, 2], label="o-dietyle benzene")
ax1.plot(t, table[:, 3], label="p-dietyle benzene")
ax1.plot(t, table[:, 4], label="m-dietyle benzene",)
ax1.legend()
ax2.legend()
ax1.set_xlabel("t")
ax1.set_ylabel("rate[%]")
ax2.set_ylabel("rate of etyle benzene[%]")
ax1.set_title("Time variation in composition")

fig.show()

# %%
