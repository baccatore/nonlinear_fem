#coding:utf8
#***************************mod.py***************************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-05-08 AM 11:42:06
# Modified  : 
# Main module for non-linear FEM. Try to break codes down to 
# smaller files
#************************************************************
import itertools

import config as cfg


def simple_product(i,j):
    return itertools(range(i), range(j))

def kron_delta(i, j):
    if i == j:
        return 1
    else:
        return 0


#Shape function
# x @ Position vector as argument
# p @ Position vector of node1
# q @ Position vector of node2
# Attribute 0->x; 1->y
# Example x(x, y) -> (x[0], x[1])
# FIXME コメント書き直し
def Ni(element, x):
    if cfg.SHAPE == 3:
        s_e = get_prlgrm(p1, p2, p3)
        #Eq. 1.50 (rf. Nonlinear FEM, p24)
        N = 1/s_e * ((p2[0]*p3[1]-p3[0]*p2[1])
                + (p2[1] - p3[1])*x[0]
                + (p3[0] - p2[0])*x[1])
    elif cfg.SHAPE == 4:
        #FIXME verify mapping from spatial coordinate to natural coordinate
        cof = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
        #p1, p2, p3, p4 = element[1:5]
        #N = [ 1/4 * (1 + xi[0]*node[pi-1][0]) * (1 + xi[1]*node[pi-1][1])
        #   for xi ,pi in zip(cof, element[1:5]) ]
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


#B Matrix
#   @i_element; Index of element
#   @node     ; Set of nodes
#   @x        ; X as global coordinate
#   @e        ; Eta as local coordinate
# This function varies depending on the number of node
# which consits of one element for each model
def b_matrix(i_element, node, x, e):
    #Four times precision is better
    #XXX Why?
    b_m = np.zeros([3,8], dtype=np.float128)
    #Nodal index which consist of the element
    i_n = np.zeros([4], dytpe=np.int8)
    i_n[0] = node[:,i_element] -1
    print(ni) #XXX Validation if substitution is successed
              #XXX Delete here once checked
    #dN/da,dN/db
    #TODO Abstractize to adopt it for higher dimension
    dN1_da = -0.25*(1.0-b)
    dN2_da =  0.25*(1.0-b)
    dN3_da =  0.25*(1.0+b)
    dN4_da = -0.25*(1.0+b)
    dN1_db = -0.25*(1.0-a)
    dN2_db = -0.25*(1.0+a)
    dN3_db =  0.25*(1.0+a)
    dN4_db =  0.25*(1.0-a)
    #Jaconbi matrix and det(J)
    j_m = np.zeros([2,2], dtype=np.float128)
    #FIXME Can be written more more easily?
    #Write down elements, can be ortho production
    for i in range(2)
        j_m[0,i] = dn1a*x[i,i]+dn2a*x[i,j]+dn3a*x[i,k]+dn4a*x[i,l] 
        j_m[1,i] = dn1b*x[i,i]+dn2b*x[i,j]+dn3b*x[i,k]+dn4b*x[i,l]
    detJ = np.det(J)
    print(j_m)   #XXX Validation
    print(detJ)  #XXX Validation
    #[B]=[dN/dx][dN/dy]
    #Can be written shorter with NumPy!
    #for i,j in simple_product(2, 4):
    bm[0,0]= J22*dn1a-J12*dn1b
    bm[0,2]= J22*dn2a-J12*dn2b
    bm[0,4]= J22*dn3a-J12*dn3b
    bm[0,6]= J22*dn4a-J12*dn4b
    bm[1,1]=-J21*dn1a+J11*dn1b
    bm[1,3]=-J21*dn2a+J11*dn2b
    bm[1,5]=-J21*dn3a+J11*dn3b
    bm[1,7]=-J21*dn4a+J11*dn4b
    bm[2,0]=-J21*dn1a+J11*dn1b
    bm[2,1]= J22*dn1a-J12*dn1b
    bm[2,2]=-J21*dn2a+J11*dn2b
    bm[2,3]= J22*dn2a-J12*dn2b
    bm[2,4]=-J21*dn3a+J11*dn3b
    bm[2,5]= J22*dn3a-J12*dn3b
    bm[2,6]=-J21*dn4a+J11*dn4b
    bm[2,7]= J22*dn4a-J12*dn4b
    return b_m


#Eq 1.52
#def u(x, y, element):
#    u = .0
#    for i in range(SHAPE):
#        u += ui(x,y) * Ni(x,y)
#    return u


#Eq. 3.167 p.125
#u2 : strain for next step
#u1 : strain for current step
#u0 : strain for one before step
def eq_of_motion(node):
    global h1, h2, h3
    h1 = kinematic_coefficient.h1()
    h2 = kinematic_coefficient.h2()
    h3 = kinematic_coefficient.h3()
    u2[i] = (h2*u1[i] + h3*u0[i]) + (P[node][i] - F[node][i])/h1
    return u2
