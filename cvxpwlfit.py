import numpy as np
from scipy.spatial import Delaunay
from scipy.sparse import lil_matrix
import scipy.interpolate
from cvxpy import *

def cvxfit(points,values):
    tri = Delaunay(points)
    n = len(points)
    ns = len(tri.simplices)
    npts = len(tri.simplices[0])
    S = lil_matrix((ns,ns), dtype=int)
    p = Variable(n)
    constraints = []
    apoints = np.array(points)

    for i in range(ns):
        neighbors = tri.neighbors[i]
        simplex = tri.simplices[i]
        # print simplex
        # print neighbors
        for j in range(npts):
            if neighbors[j] == -1: continue
            i2, n2 = i, neighbors[j]
            if (i2 > n2):
                temp = i2
                i2 = n2
                n2 = temp
            if S[i2, n2] == 0: 
                S[i2, n2] = simplex[j]+1
                # print simplex[j]
            else:
                # [ ] calc lambda, mu
                v_opp = S[i2, n2] - 1
                S[i2, n2] = 0 # remove the element
                A = np.array(apoints[simplex].transpose())
                p_opp = apoints[v_opp]
                b = np.hstack((A[:,j], 1.))
                A[:,j] -= p_opp
                mu = np.ones(npts)
                mu[j] = 0.
                A2 = np.vstack((A, mu))
                bc = np.linalg.solve(A2, b)
                # constraints += [ p[simplex[j]] + bc[v_opp] >= bc.dot(p[simplex]) ]
                constraints += [p[simplex[j]] + bc[j] * p[v_opp] >= bc.T * p[simplex] ]
                # [ ] impose constraints
    # [ ] Solve cvx
    prob = Problem(Minimize(norm(p - values)), constraints)
    prob.solve()
    # print p.value.T.tolist()
    # return adjusted points in list format
    new_values = []
    for i in range(n):
        new_values += [p.value[i,0]]
    # print new_values
    return scipy.interpolate.LinearNDInterpolator(tri, new_values, fill_value=0)



if __name__ == "__main__":
    x = np.array([0, 0, 1, 1])
    y = np.array([ 0, 1.1, 0, 1 ])
    z = np.array([5.0, 2.0, 3.0, 6.0])
    # Create coordinate pairs
    points = list(zip(x, y))
    values = np.array([5.0, 2.0, 3.0, 6.0])
    cvxfit(points, values)