'''
https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.Delaunay.html
'''

import numpy as np
points = np.array([[0, 0], [0, 1.1], [1, 0], [1, 1]])
from scipy.spatial import Delaunay
tri = Delaunay(points)
# import matplotlib.pyplot as plt
# plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
# plt.plot(points[:,0], points[:,1], 'o')
# plt.show()
# print tri.simplices
# print points[tri.simplices]
# print tri.neighbors[1]
# print points[tri.simplices[1,1]]
# p = np.array([(0.1, 0.2), (1.5, 0.5)])
# b = tri.transform[1,:2].dot(p - tri.transform[1,2])
# print np.c_[b, 1 - b.sum(axis=1)]
from scipy.sparse import lil_matrix
ns = len(tri.simplices)
np = len(tri.simplices[0])
A = lil_matrix((ns,ns))
for i in range(0, ns):
    neighbors = tri.neighbors[i]
    simplex = tri.simplices[i]
    for j in range(0, np):
        if neighbors[j] == -1: continue
        i2, n2 = i, neighbors[j]
        if (i2 > n2):
            temp = i2
            i2 = n2
            n2 = temp
        if A[i2,n2] == 0: 
            A[i2,n2] = 1
            print i2,n2

'''
def sparseSym(rank, density=0.01, format='coo', dtype=None, random_state=None):
  density = density / (2.0 - 1.0/rank)
  A = scipy.sparse.rand(rank, rank, density=density, format=format, dtype=dtype, random_state=random_state)
  return (A + A.transpose())/2

import scipy.sparse as sparse
sparse.rand(5, 5, density=0.1)
'''
