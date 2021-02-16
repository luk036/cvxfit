import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate
from cvxpwlfit import *
import mpl_toolkits.mplot3d

x = np.array([-4386795.73911443, -1239996.25110694, -3974316.43669208,
               1560260.49911342,  4977361.53694849, -1996458.01768192,
               5888021.46423068,  2969439.36068243,   562498.56468588,
               4940040.00457585])

y = np.array([ -572081.11495993, -5663387.07621326,  3841976.34982795,
               3761230.61316845,  -942281.80271223,  5414546.28275767,
               1320445.40098735, -4234503.89305636,  4621185.12249923,
               1172328.8107458 ])

z = np.array([ 4579159.6898615 ,  2649940.2481702 ,  3171358.81564312,
               4892740.54647532,  1862475.79651847,  2707177.605241  ,
               2059175.83411223,  3720138.47529587,  4345385.04025412,
               3847493.83999694])

x = x / 10000000.
y = y / 10000000.
z = z / 10000000.
#z = z + 0.1*np.random.randn(10)

# Create coordinate pairs
cartcoord = list(zip(x, y))

X = np.linspace(min(x), max(x))
Y = np.linspace(min(y), max(y))
X, Y = np.meshgrid(X, Y)

# Approach 1
interp = scipy.interpolate.LinearNDInterpolator(cartcoord, z, fill_value=0)
Z0 = interp(X, Y)
plt.figure()
#plt.pcolormesh(X, Y, Z0)
#plt.colorbar() # Color Bar
ax=plt.subplot(111,projection='3d')
ax.plot_surface(X,Y,Z0,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)
plt.show()

# Convex fit
cinterp = cvxfit(cartcoord, -z)
Z1 = cinterp(X, Y)
plt.figure()
#plt.pcolormesh(X, Y, -Z1)
#plt.colorbar() # Color Bar
ax=plt.subplot(111,projection='3d')
ax.plot_surface(X,Y,-Z1,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)
plt.show()
