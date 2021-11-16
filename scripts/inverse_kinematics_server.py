#!/usr/bin/env python

from __future__ import print_function

from rbe500project.srv import inverse_kinematics_,inverse_kinematics_Response
import rospy
import math

def inverse_kinematics(req):
    print("Returning the q1, q2 and q3 for [%s  %s  %s] values of "%(req.x, req.y, req.z))
    l1 =1
    l2 = 1
    l3 = 1
    r2 = (req.x*req.x)+(req.y*req.y)
    D = (r2-(l2*l2)-(l3*l3))/(2*l2*l3)
    q1 = math.atan2(math.sqrt(1-(D*D)),D) - math.atan2((l3*math.sin(q2)),(l2+l3*math.cos(q2)))
    q2 = math.atan2(math.sqrt(1-(D*D)),D)
    q3 = req.z
    # q1=3
    # q2=-1
    # q3=2

    return inverse_kinematics_Response(q1,q2,q3)

def inverse_kinematics_server():
    rospy.init_node('inverse_kinematics_server')
    s = rospy.Service('inversekinematics', inverse_kinematics_, inverse_kinematics)
    print("Ready to find the inverse kinematics")
    rospy.spin()

if __name__ == "__main__":
    inverse_kinematics_server()
