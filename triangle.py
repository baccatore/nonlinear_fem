#conding:utf8
#**********************__triangle.py__***********************
# Author    : Yuichiro SUGA
# Email     : yuichiro.suga@centraliens-lille.org
# Created   : 2018-04-25 PM 04:56:38
# Modified  : 
# Manipulate and calculate vectors on 2d plane 
#************************************************************
import numpy as np

#Get area of triangle p1-p2-p3
#Refers nodes in *anti-clockwise*
def get_area(p1, p2, p3):
    area = 1/2 * ( p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]
            - p1[0]*p3[1] - p2[0]*p1[1] - p3[0]*p2[1] )
    if area < 0:
        raise NameError('Clockwise triangle, Element area got negative')
    return area

if __name__ == "__main__":
    test_element = np.array([[.0,.0],[1.,.0],[0.0,1.0]])
    print(test_element)
    print(get_area(test_element[0],test_element[1],test_element[2]))
    
    test_element *= 2
    print(test_element)
    print(get_area(test_element[0],test_element[1],test_element[2]))
    
    test_element += 2
    print(test_element)
    print(get_area(test_element[0],test_element[1],test_element[2]))

    test_element = np.array([[.0,.0],[1.0,.0],[0.5,.866]])
    print(test_element)
    print(get_area(test_element[0],test_element[1],test_element[2]))

    test_element *= 2
    print(test_element)
    print(get_area(test_element[0],test_element[1],test_element[2]))
    
    test_element += 2
    print(test_element)
    print(get_area(test_element[0],test_element[1],test_element[2]))
