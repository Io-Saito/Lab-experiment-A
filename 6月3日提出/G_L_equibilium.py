import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np


data_frame = pd.read_csv("Book2.prn",sep="\s+",header=None)
print(data_frame)
data_frame.columns=["x","y","T"]
arr = data_frame.values
print(arr)
x=arr[:,0]
T=arr[:,2]
y=arr[:,1]

fig=plt.figure(figsize=(12, 6))
ax1=fig.add_subplot(1,2,1)
ax1.scatter(x,T,c="red",label="liquid phese",s=2)
ax1.scatter(y,T,c="blue",label="gas phese",s=2)
ax1.set_title('gas-liquid equibilium curve\n in ethanol-water mixed solution')
ax1.set_xlabel('x1,y1')
ax1.set_ylabel('tempeture')
ax1.legend(loc='upper right')


ax2=fig.add_subplot(1,2,2)
ax2.scatter(x,y,c="green",s=2)
ax2.set_title('composition curve at equibilium \nin ethanol-water mixed solution ')
ax2.set_xlabel("x:liquid phese")
ax2.set_ylabel("y:gas phese")
ax2.legend(loc="upper left")
plt.show()
