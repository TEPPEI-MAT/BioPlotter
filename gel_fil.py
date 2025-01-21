#import module#
import pandas as pd
import matplotlib.pyplot as plt
import os


#Path#
input_path = "/Users/matsuda_teppei/Library/CloudStorage/OneDrive-愛媛大学/Nm6_Matsuda/000_Tokushima/24120501_SEC_sizeM.csv"
df = pd.read_csv(input_path, skiprows=1)
base, _ = os.path.splitext(input_path) 
output_path = f"{base}.png"  


#Plot#
fig,ax = plt.subplots(figsize=(12,8))
x = df["UV(280 nm)_volume"]
y = df["UV(280 nm)_mAU"]

ax.plot(x,y,color = "#000000",lw = 1.5,zorder=2) #色の設定#

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().yaxis.set_ticks_position('left')
plt.gca().xaxis.set_ticks_position('bottom')
ax.set_xlabel('Volume [ml]',size=25)
ax.set_ylabel('Absorbance at 280 nm [mAu]',size=25)
plt.yticks(size=25, color="#2b2b2b")
plt.xticks(size=25, color="#2b2b2b")
#plt.xlim(3, 30) #横軸の幅#
#plt.ylim(-5, 15) #縦軸の幅#

#plt.show() #確認したい時は頭の＃を消す

#save figure#
plt.savefig(output_path, dpi = 1200, bbox_inches='tight')
