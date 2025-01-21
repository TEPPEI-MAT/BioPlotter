#import module#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

#define function#
def Single_exp(x, a, b, c):
    return a * np.exp(-b * x) + c

def graph_plot(max, a, b, c):
  limit = max + max/10
  x = []
  y = []
  lt = range(0,100000 + 1)
  for j in lt:
    i = max/100000 * j
    x.append(i)
    y.append(Single_exp(i, a, b, c))
  return x, y

#dataframe#
df = pd.read_csv("test.csv")
df1 = df.groupby("time",as_index = False,sort = False).describe()["signals"]
df2 = df.query("replicates == 'rep1'")
df1["time"] = df2["time"]
df3,cov = curve_fit(Single_exp,df["time"],df["signals"],p0=[-1.39100870e+04 , 4.12237895e-02, 1.40461014e+04])
xs, ys = graph_plot(df1["time"].max()+1,df3[0],df3[1], 1.40461014e+04)
df4 = pd.DataFrame({'time': xs, 'signals': ys})

#drawing plot#
fig,ax = plt.subplots(figsize=(8,6))
x = df4["time"]
y = df4["signals"]
yerr = df1["std"]
ax.plot(x,y,color = "#51A789",lw = 4,zorder=2)
x1 = df1["time"]
y1 = df1["mean"]
x2 = df["time"]
y2 = df["signals"]
ax.errorbar(x1,y1,yerr = yerr,ecolor = "#000000",capsize = 10,fmt = "go",markersize=0,capthick = 1.5,elinewidth = 1.5,zorder=2)
ax.scatter(x2,y2,color = "#51A789",edgecolor ="#51A789",s = 100, linewidth=1.5, zorder=2)

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().yaxis.set_ticks_position('left')
plt.gca().xaxis.set_ticks_position('bottom')
ax.set_xlabel('Time [min]',size=22)
ax.set_ylabel('$^\mathrm{3}$H-methyl group incorporation [dpm]',size=18)
plt.yticks(size=25, color="#2b2b2b")
plt.xticks(size=25, color="#2b2b2b")
#plt.show()

#save figure#
plt.savefig("test.png",dpi = 1200,bbox_inches='tight', transparent=True)
