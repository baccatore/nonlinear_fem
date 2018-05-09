#coding:utf8
#************************__main.py__*************************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-04-25 PM 04:56:38
# Modified  : 
# Non-linear Finite Element Method 
#************************************************************
#NOTE 2次元三角形要素を想定
import numpy as np
import time

import config as cfg
import mod as nlfem
import read_mesh
import kinematic_coefficient


if __name__ == "__main__":
    #Run stopwatch
    start = time.time()
    
    #1. Read mesh data file
    node, shell = read_mesh.read_mesh()
    #print(nlfem.Ni(shell[10], [.5, .5]))
    #N = get_N([0.5,0.5]
    print(cfg.h1)
    print(node)

    #2. Determination of Delta t

    #3. Configuration nodal stress

    #4. Calculation of nodal displacement

    #5. Calculation of stress and strain

    #6. Update displacement

    #7. Update material parameter

    #8. Output result

    #Stop stopwatch
    dtime = time.time() - start
    print("time: {0:.3f}".format(dtime) + ' sec')
