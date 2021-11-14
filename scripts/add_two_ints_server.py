#!/usr/bin/env python

from __future__ import print_function

from rbe500project.srv import AddTwoInts,AddTwoIntsResponse
import rospy
import math

def handle_add_two_ints(req):
    print("Returning the q1, q2 and q3 for [%s  %s  %s] values of "%(req.x, req.y, req.z))
    q1=3
    q2=-1
    q3=2

    return AddTwoIntsResponse(q1,q2,q3)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()