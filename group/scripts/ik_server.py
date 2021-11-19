#!/usr/bin/env python
import rospy
import math
from group.srv import ik,ikResponse

def handle_add_two_ints(req):
    l1 =1
    l2 = 1
    l3 = 1
    r2 = (req.x*req.x)+(req.y*req.y)
    D = (r2-(l2*l2)-(l3*l3))/(2*l2*l3)
    q1 = math.atan2(math.sqrt(1-(D*D)),D) - math.atan2((l3*math.sin(q2)),(l2+l3*math.cos(q2)))
    q2 = math.atan2(math.sqrt(1-(D*D)),D)
    q3 = req.z
    return ikResponse(q1, q2, q3)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    rospy.Service('inverse kinematics', ik , handle_add_two_ints)
    print("Ready to calculate ik")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
