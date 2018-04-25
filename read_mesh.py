#*********************__read_mesh.py__***********************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-04-25 PM 10:44:14
# Modified  : 
# Read mesh data saved as .pc 
#************************************************************
import re


if 'shell' 'node' not in globals():
    node = []
    shell = []

def read_mesh():
    global node, mesh
    with open("node.dat", "r") as data:
        for line in data:
            node.append([float(x) for x in line.split()]) #Implicitly splits by space

    with open("shell.dat", "r") as data:
        for line in data:
            shell.append([int(x) for x in line.split()]) #Implicitly splits by space
    
    return (node, shell)

if __name__ == "__main__":
    read_mesh()
    for n in node:
        print(n)
    for s in shell:
        print(s)
