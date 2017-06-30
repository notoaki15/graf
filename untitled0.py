
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D


#ｘ，ｙの範囲
x=np.arange(-3,6,0.25,)
y=np.arange(-3,6,0.25)
#形
X,Y=np.meshgrid(x,y)
Z = np.sin(Y)


#座標を3Dにする
fig = plt.figure()
ax = Axes3D(fig)

#描画
ax.plot_wireframe(X,Y,Z,color='orangered')

#表示
plt.plot(x,y,'r+')
plt.show()
