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
df = pd.read_csv("/Users/matsuda_teppei/Documents/Nm6/070_TK1257_timecourse/timecourse.csv")
df1 = df.groupby("time",as_index = False,sort = False).describe()["signals"]
df2 = df.query("replicates == 'rep1'")
df1["time"] = df2["time"]
df3,cov = curve_fit(Single_exp,df["time"],df["signals"],p0=[-1.39100870e+04 , 4.12237895e-02, 1.40461014e+04])
xs, ys = graph_plot(df1["time"].max()+1,df3[0],df3[1], 1.40461014e+04)
df4 = pd.DataFrame({'time': xs, 'signals': ys})
print(df3)
dfb = pd.read_csv("/Users/matsuda_teppei/Documents/RCT/037_revised_data/NTP_bar.csv")
df10 = dfb[dfb["type"] == "one"]
df25 = dfb[dfb["type"] == "two"]
df375 = dfb[dfb["type"] == "three"]
df5 = dfb[dfb["type"] == "four"]


t1,p1 = stats.ttest_rel(df10["signal"],df25["signal"])
t2,p2 = stats.ttest_rel(df375["signal"],df25["signal"])
t3,p3 = stats.ttest_rel(df5["signal"],df25["signal"])

print(p1)
print(p2)
print(p3)

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
#ax.errorbar(x1,y1,yerr = yerr,ecolor = "#0081FF",capsize = 10,fmt = "go",markersize=0,capthick = 1.5,elinewidth = 1.5,zorder=2)
#ax.errorbar(x1,y1,yerr = yerr,color = "#c3d82d",ecolor = "#1e1210",capsize = 7,fmt = "go",markersize=10,markeredgecolor = "#1e1210")
#ax.scatter(x1,y1,color = "#0081FF",edgecolor ="#0081FF",s = 75, linewidth=1, zorder=2)
#ax.scatter(x2,y2,color = "#0081FF",edgecolor ="#2b2b2b",s = 75, linewidth=0.5, zorder=2,marker="D",alpha=0.8)

ax.errorbar(x1,y1,yerr = yerr,ecolor = "#000000",capsize = 10,fmt = "go",markersize=0,capthick = 1.5,elinewidth = 1.5,zorder=2)

#ax.scatter(x2,y2,color = "#0BBF00",edgecolor ="#2b2b2b",s = 75, linewidth=0.5, zorder=2,marker="D",alpha=0.8)
ax.scatter(x2,y2,color = "#51A789",edgecolor ="#51A789",s = 100, linewidth=1.5, zorder=2)
#ax.scatter(x2,y2,color = "#0BBF00",s = 100,  zorder=2,alpha=0.1)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().yaxis.set_ticks_position('left')
plt.gca().xaxis.set_ticks_position('bottom')
ax.set_xlabel('Time [min]',size=22)
ax.set_ylabel('$^\mathrm{3}$H-methyl group incorporation [dpm]',size=18)
plt.yticks(size=25, color="#2b2b2b")
plt.xticks(size=25, color="#2b2b2b")
plt.show()


#save figure#
#plt.savefig("/Users/matsuda_teppei/Documents/RCT/037_revised_data/NTP_R3.png",dpi = 1200,bbox_inches='tight')

#plt.savefig(r"C:\Users\oraor\OneDrive - 愛媛大学\RCT\000_ROCKET_paper_data\fig4\material\His_Primer_vol.png",dpi = 1200,bbox_inches='tight')

#plt.savefig("/Users/matsuda_teppei/Documents/University/meeting/M2/2024/Timecourse.png",dpi = 1200,bbox_inches='tight', transparent=True)
