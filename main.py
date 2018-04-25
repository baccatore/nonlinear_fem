#coding:utf8
#************************__main.py__*************************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-04-25 PM 04:56:38
# Modified  : 
# Non-linear Finite Element Method 
#************************************************************
#XXX 2次元三角形要素を想定
import kinematic_coefficient
import numpy as np

import read_mesh

#Constant
RHO = 1.0  #Mass density
D_T  = .01  #Time step
C   = .5   #Attenuate coefficient
DIMENSION = 2
SHAPE = 4 #Number of nodes to one element consist of
NODE = []
SHELL = []


#def K():
#    return


#u_t+dt
#def u_t2(): 
#    return

#Shape function
# x @ Position vector as argument
# p @ Position vector of node1
# q @ Position vector of node2
# Attribute 0->x; 1->y
# Example x(x, y) -> (x[0], x[1])
# FIXME コメント書き直し
def Ni(element, x):
    if SHAPE == 3:
        s_e = get_prlgrm(p1, p2, p3)
        #Eq. 1.50 (rf. Nonlinear FEM, p24)
        N = 1/s_e * ((p2[0]*p3[1]-p3[0]*p2[1]) + (p2[1] - p3[1])*x[0] + (p3[0] - p2[0])*x[1])
    elif SHAPE == 4:
        #FIXME verify mapping from spatial coordinate to natural coordinate
        cof = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
        #p1, p2, p3, p4 = element[1:5]
        #N = [ 1/4 * (1 + xi[0]*NODE[pi-1][0]) * (1 + xi[1]*NODE[pi-1][1]) for xi ,pi in zip(cof, element[1:5]) ]
        N = [ 1/4 * (1 + xi[0]*x[0]) * (1 + xi[1]*x[1]) for xi in cof ]
    else:
        raise NameError('Constant "SHAPE" is invalid!')
    return N

#Get area of parallelogram p1-p2-p3
# Refers nodes in *anti-clockwise*
def get_prlgrm(p1, p2, p3):
    area = ( p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]
            - p1[0]*p3[1] - p2[0]*p1[1] - p3[0]*p2[1] )
    if area < 0:
        raise NameError('Clockwise triangle, Element area got negative')
    return area

#Current material point: X
def get_N(X):
    N = np.zeros((DIMENSION, SHAPE * DIMENSION))
    N = [[Ni(X, p2, p3), .0],
         [.0, Ni(X, p2, p3)],
         [Ni(X, p3, p1), .0],
         [.0, Ni(X, p3, p1)]
         [Ni(X, p1, p2), .0],
         [.0, Ni(X, p1, p2)]]
    return N

#Eq 1.52
def u(x, y, element):
    u = .0

    for i in range(SHAPE):
        u += ui(x,y) * Ni(x,y)
    return u


def v(x,y):
    return u(x,y)

if __name__ == "__main__":
    #1. Reading node, elements from mesh data file
    NODE, SHELL = read_mesh.read_mesh()
    print(Ni(SHELL[10], [.5, .5]))
    #N = get_N([0.5,0.5])
