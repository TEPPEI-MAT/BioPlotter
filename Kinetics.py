#import module#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import seaborn as sns

#define finction#
#converter of dpm to mol
def dpm_to_mol(dataframe):
    return dataframe.loc["dpm"]/60*3.7*10**-10
    
def MM(x,Vmax,km): 
    return  Vmax*x/(x+km)

def graph_plot(max, Vmax, km): 
  limit = max + max/10
  x = []
  y = []
  lt = range(0,100 + 1)
  for j in lt:
    i = max/100 * j
    x.append(i)
    y.append(MM(i,Vmax,km))
  return x, y


#dataframe#
df = pd.read_csv("test.csv")
use = (3.5 / 40765.44) * 0.875 * 10 ** 6 #amount of enzyme
df["mol"] = df.apply(dpm_to_mol,axis = 1)*6 * 10**9
df1 = df.groupby("conc",as_index = False,sort = False).describe()["mol"]
df2 = df.query("replicates == 'rep1'")
df1["conc"] = df2["conc"]
df3,cov = curve_fit(MM,df["conc"],df["mol"],p0=[0, 0])
xs, ys = graph_plot(df1["conc"].max(),df3[0],df3[1])
df4 = pd.DataFrame({'conc': xs, 'mol': ys})
Vmax = df3[0]
Km = df3[1]
print(Vmax)
print(Km)

#drawing plot#
fig,ax = plt.subplots(figsize=(8,6))
x = df4["conc"]
y = df4["mol"]
yerr = df1["std"]
ax.plot(x,y,color = "#51A789",zorder=1,lw = 4,)
x1 = df1["conc"]
y1 = df1["mean"]
x2 = df["conc"]
y2 = df["mol"]
ax.set_xlabel('x',size=25)
ax.set_ylabel('y',size=25)
ax.scatter(Km, Vmax / 2, color='#E13980', zorder=3)
ax.scatter(x2, y2, color="#0BBF00", edgecolor="#1e1210", s=75, alpha=0.8)
ax.vlines(Km,0, Vmax/2,color='#E13980',linestyle = "dashed", zorder=3)
ax.text(df1.iat[1,8],2*10**-9,"Vmax = "+str(Vmax))
ax.text(df1.iat[1,8],0,"Km = "+str(Km))
ax.errorbar(x1,y1,yerr = yerr,ecolor = "#000000",capsize = 10,fmt = "go",markersize=0,capthick = 1.5,elinewidth = 1.5,zorder=2)
ax.scatter(x2,y2,color = "#51A789",edgecolor ="#51A789",s = 100, linewidth=1.5, zorder=3)


plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().yaxis.set_ticks_position('left')
plt.gca().xaxis.set_ticks_position('bottom')
plt.yticks(size=25, color="#2b2b2b")
plt.xticks(size=25, color="#2b2b2b")
#plt.show()
plt.savefig("test.png",dpi = 1200,bbox_inches='tight', transparent=True)

