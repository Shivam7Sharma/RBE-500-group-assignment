#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from group.srv import *
import numpy as np
import math

def inverse_kinematics_client(x, y,z):
    rospy.wait_for_service('inversekinematics')
    try:
        inversekinematics = rospy.ServiceProxy('inversekinematics', inverse_kinematics_)
        print(type(x))
        resp1 = inversekinematics(x,y,z)
        my_array = np.array([resp1.q1,resp1.q2,resp1.q3])
        print(resp1)
        return my_array
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y z]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
        z= float(sys.argv[3])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting q1,q2 and q3 for %s %s %s"%(x, y,z))
    arr=inverse_kinematics_client(x, y,z)
    print("values for the joint angles of end pose %s %s %s are  = %s %s %s"%(x, y,z,arr[0],arr[1],arr[2]))
