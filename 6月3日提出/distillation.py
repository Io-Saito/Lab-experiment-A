import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
#与えられた気液平衡データをゲット
data_frame = pd.read_csv("Book2.csv",sep=",",header=None)
print(data_frame)
data_frame.columns=["T","x","y"]
arr = data_frame.values
print(arr)
x=arr[:,1]
T=arr[:,0]
y=arr[:,2]
#多項式近似
res_1=np.polyfit(x, T, 3)
res_2=np.polyfit(y,T,3)
x_=np.poly1d(res_1)(x)
y_=np.poly1d(res_2)(y)
#プロット
fig=plt.figure(figsize=(12, 6))
ax1=fig.add_subplot(1,2,1)
#生データ
ax1.scatter(x, T, label="liquid phese", c="b", s=4)
ax1.scatter(y, T, label="gas phese", c="r", s=4)
#近似式
ax1.plot(x, x_, label="liquid phese-approximation", c="m")
ax1.plot(y, y_, label="gas phese-approximation", c="g")
ax1.set_title('gas-liquid equibilium curve\n in ethanol-water mixed solution')
ax1.set_xlabel('x1,y1')
ax1.set_ylabel('tempeture')
ax1.legend(loc='upper right')
plt.show()
