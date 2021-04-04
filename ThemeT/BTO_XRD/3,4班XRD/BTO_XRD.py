# %%
import japanize_matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc
from scipy import signal
from scipy.fftpack import fft, fftshift
import pytablewriter

# %%"

num = 6
b = np.ones(num)/num

df = pd.read_csv(
    "201209_3班XRD.csv", header=59, delimiter="\t")
theta_si = np.array(df["; 2THETA"])
spectrum_si = np.array(df["Cnt2_D1"])

df2 = pd.read_csv(
    "201209_4班XRD.csv", header=59, delimiter="\t")
theta_sipt = np.array(df2["; 2THETA"])
spectrum_sipt = np.array(df2["Cnt2_D1"])

# %%
lam = 1.54068*(10**-10)


def move_mean(list):
    return np.convolve(list, b, mode="same")


def peak(list, num):
    return signal.argrelmax(list, order=num)


def lattice_constant(theta):
    d = lam/(2*np.sin(np.radians(theta/2)))*(10**10)
    return d  # [Å]


def table(num, spectrum, theta):
    peak_index = peak(move_mean(spectrum), num)[0]
    peak_df = pd.DataFrame(np.array((np.array(peak_index), theta[peak_index], move_mean(
        spectrum)[peak_index], lattice_constant(theta[peak_index]))).T)
    return peak_df


peak1 = table(150, spectrum_si, theta_si)
display(peak1)
display(peak1.columns)
peak_2 = table(40, spectrum_sipt, theta_sipt)
peak2 = peak_2[peak_2[2] > 35]
display(peak2)
# %%
fig = plt.figure()
ax1 = fig.add_subplot()
ax1.plot(theta_si, spectrum_si, label="オリジナル")
ax1.plot(theta_si, move_mean(spectrum_si), label="移動平均")
ax1.scatter(peak1[1], peak1[2]+100, color="black", marker="v", label="ピーク")
ax1.set_title("BTO XRD測定(Si基板)")
ax1.set_xlabel("2θ[°]")
ax1.set_yscale("log")
ax1.set_ylabel("count(log)")
ax1.legend(loc="upper left")
fig.show()


# %%

fig2 = plt.figure()
ax2 = fig2.add_subplot()
ax2.plot(theta_sipt, spectrum_sipt, label="オリジナル")
ax2.plot(theta_sipt, move_mean(spectrum_sipt), label="移動平均")
ax2.scatter(peak2[1], peak2[2]+100, color="black", marker="v", label="ピーク")
ax2.set_title("BTO XRD測定(Si-Pt基板)")
ax2.set_xlabel("2θ[°]")
ax2.set_yscale("log")
ax2.set_ylabel("count(log)")
ax2.legend(loc="upper left")
fig2.show()
display(peak2)

# %%
writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(peak2)
writer.write_table()

# %%
