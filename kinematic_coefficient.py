import config as cfg

def h1():
    return (cfg.RHO/cfg.D_T**2) + cfg.C/(2*cfg.D_T)

def h2():
    return -2*cfg.RHO/(cfg.D_T**2) 

def h3():
    return (cfg.RHO/cfg.D_T**2) - cfg.C/(2*cfg.D_T)

cfg.h1 = h1()
cfg.h2 = h2()
cfg.h3 = h3()
