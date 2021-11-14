#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from rbe500project.srv import *
import numpy as np
import math

def add_two_ints_client(x, y,z):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp1 = add_two_ints(x, y,z)
        my_array = np.array([resp1.q1,resp1.q2,resp1.q3])
        return my_array
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z= int(sys.argv[3])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting q1,q2 and q3 for %s %s %s"%(x, y,z))
    arr=add_two_ints_client(x, y,z)
    print("values for the joint angles of end pose %s %s %s are  = %s %s %s"%(x, y,z,arr[0],arr[1],arr[2]))