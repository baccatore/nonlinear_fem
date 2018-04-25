
RHO = 1.0  #Mass density
D_T  = .01  #Time step
C   = .5   #Attenuate coefficient


def h1():
    global RHO, D_T, C
    return (RHO/D_T**2) + C/(2*D_T)


def h2():
    global RHO, D_T
    return -2*RHO/(D_T**2) 


def h3():
    global RHO, D_T
    return (RHO/D_T**2) - C/(2*D_T)
