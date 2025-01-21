#import module#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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
df = pd.read_csv("tset.csv")
df1 = df.groupby("conc",as_index = False,sort = False).describe()["dpm"]
df2 = df.query("replicates == 'rep1'")
df1["conc"] = df2["conc"]
df3,cov = curve_fit(IC50,df["conc"],df["dpm"], p0=[ 0.58228885 ,-6.82666993  ,6.40252001 , 0.09452325])
xs, ys = graph_plot(df1["conc"].max()+1,df3[0],df3[1],df3[2],df3[3])
df4 = pd.DataFrame({'conc': xs, 'dpm': ys})
print(df3)
print(df["dpm"])

#drawing plot#
fig,ax = plt.subplots(figsize=(8,6))
x = df4["conc"]
y = df4["dpm"]
yerr = df1["std"]
ax.plot(x,y,color = "#000000",lw =1.5,zorder=2)
x1 = df1["conc"]
y1 = df1["mean"]
x2 = df["conc"]
y2 = df["dpm"]
ax.errorbar(x1,y1,yerr = yerr,ecolor = "#000000",color = "#000000",capsize = 10,fmt = "go",markersize=10,capthick = 1,elinewidth = 1,zorder=2)

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().yaxis.set_ticks_position('left')
plt.gca().xaxis.set_ticks_position('bottom')
ax.set_xlabel('Time [h]',size=24)
ax.set_ylabel('Optical density (660 nm)',size=24)
plt.yticks(size=25, color="#2b2b2b")
plt.xticks(size=25, color="#2b2b2b")
plt.xlim(2.5, 15)

#plt.show()
plt.savefig("/Users/matsuda_teppei/Library/CloudStorage/OneDrive-愛媛大学/Nm6_Matsuda/000_manuscript/figure/material/growth_85.png",dpi = 1200,bbox_inches='tight')
