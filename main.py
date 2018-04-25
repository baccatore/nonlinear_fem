#conding:utf8
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

#Constant
RHO = 1.0  #Mass density
D_T  = .01  #Time step
C   = .5   #Attenuate coefficient
DIMENSION = 2
SHAPE = 3 #Number of nodes to one element consist of

#Elements
E = [ (0.0, 0.0), (1.0, 0.0), (0.0, 1.0), (1.0, 1.0) ]

#Displacement
# 10% compression
d_e = [.0, -.1, 0., -.1, 0., .0]


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
def Ni(x, p2, p3):
    s_e = get_prlgrm(p1, p2, p3)
    #Eq. 1.50 (rf. Nonlinear FEM, p24)
    n1 = 1/s_e * ((p2[0]*p3[1]-p3[0]*p2[1]) + (p2[1] - p3[1])*x[0] + (p3[0] - p2[0])*x[1])
    return n1

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

if __name__ == "__main__":
    N = get_N([0.5,0.5])
