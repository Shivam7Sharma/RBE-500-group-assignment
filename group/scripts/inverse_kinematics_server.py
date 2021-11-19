#!/usr/bin/env python3
from group.srv import inverse_kinematics_,inverse_kinematics_Response #change the package name(group.srv)
import rospy
import math
import numpy as np

def ik_service(req):
    #print("Returning the q1, q2 and q3 for [%s  %s  %s] values of "%(req.x, req.y, req.z))
    l1 = 1
    l2 = 1
    l3 = 1
    x = req.x
    y = req.y
    z = req.z
    r = math.sqrt((x**2)+(y**2))
    alpha = math.atan2(y,x)
    D = ((r**2)-(l2**2)-(l3**2))/(2*l2*l3)
    q3 = (z - l1)
    #print('joint3:',q3)
    sq = math.sqrt(1-(D**2))
    q2 = math.atan2(sq,D)
    #print('joint2 :',q2)
    a1 = l3*math.sin(q2)
    a2 = l2+(l3*math.cos(q2))
    beta = math.atan2(a1,a2)
    q1 = (alpha - beta)
    q1 = np.rad2deg(q1)
    q2 = np.rad2deg(q2)
    print('[q1,q2,q3] =',q1,q2,q3)
    return inverse_kinematics_Response(q1,q2,q3)

def inverse_kinematics_server():
    rospy.init_node('inverse_kinematics_server')
    s = rospy.Service('inversekinematics', inverse_kinematics_, ik_service)
    print("Ready to find the inverse kinematics")
    rospy.spin()

if __name__ == "__main__":
    inverse_kinematics_server()
