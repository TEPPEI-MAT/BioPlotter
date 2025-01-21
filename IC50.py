#import module#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

#define function#
def IC50(x, a, b, c, d):
    return d + (a - d)/(1 + (x/c)**b)

def graph_plot(max, a, b, c, d):
  limit = max + max/10
  x = []
  y = []
  lt = range(0,100000 + 1)
  for j in lt:
    i = max/100000 * j
    x.append(i)
    y.append(IC50(i, a, b, c, d))
  return x, y

a=7643.00913
b=1.80542
c=29.73884
d=4166.04794
#dataframe#
df = pd.read_csv("test.csv")
df1 = df.groupby("conc",as_index = False,sort = False).describe()["dpm"]
df2 = df.query("replicates == 'rep1'")
df1["conc"] = df2["conc"]
df3,cov = curve_fit(IC50,df["conc"],df["dpm"], p0=[0.99857839,  1.80542466, 29.73883941,  0.54430465])
xs, ys = graph_plot(df1["conc"].max()+1,df3[0],df3[1],df3[2],df3[3])
df4 = pd.DataFrame({'conc': xs, 'dpm': ys})

#drawing plot#
fig,ax = plt.subplots(figsize=(6,8))
x = df4["conc"]
y = df4["dpm"]
yerr = df1["std"]
ax.plot(x,y,color = "#331D8A",lw =4,zorder=2)
x1 = df1["conc"]
y1 = df1["mean"]
x2 = df["conc"]
y2 = df["dpm"]
ax.errorbar(x1,y1,yerr = yerr,ecolor = "#000000",capsize = 10,fmt = "go",markersize=0,capthick = 2,elinewidth = 2,zorder=2)
ax.scatter(x2,y2,color = "#331D8A",edgecolor ="#331D8A",s = 100, linewidth=2, zorder=2)
df = pd.read_csv("test.csv")
fifty= (max(df1["mean"]) + min(df1["mean"]))/2

df11 = df.groupby("conc",as_index = False,sort = False).describe()["dpm2"]
df2 = df.query("replicates == 'rep1'")
df11["conc"] = df2["conc"]

fifty2= (max(df11["mean"]) + min(df11["mean"]))/2
IC=(c*((a-d)/(fifty2-d)-1)**(1/b))
ax.scatter(IC, fifty, color='#FF6100', zorder=3)
ax.vlines(IC,min(df["dpm"]), fifty,color='#FF6100',linestyle = "dashed", zorder=3)
ax.vlines(IC,0, fifty,color='#FF6100',linestyle = "dashed", zorder=3)

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().yaxis.set_ticks_position('left')
plt.gca().xaxis.set_ticks_position('bottom')
ax.set_xlabel('x',size=20)
ax.set_ylabel('y',size=20)
plt.yticks(size=25, color="#2b2b2b")
plt.xticks(size=25, color="#2b2b2b")
#plt.xlim(-1, 85)
#plt.ylim(0, 1.25)

#plt.show()

#save figure#
plt.savefig("test.png",dpi = 1200,bbox_inches='tight', transparent=True)
