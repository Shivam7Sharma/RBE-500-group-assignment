#!/usr/bin/env python
import rospy
import math
import numpy as np 
from sensor_msgs.msg import JointState
from std_msgs.msg import String

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    #msg = JointState()
    q1 = data.velocity[0]
    q2 = data.velocity[1]
    q3 = data.velocity[2]
    vel = [[q1], [q2], [q3]]
    #print('[q1,q2,q3] =',q1,q2,q3)
    J = [[-math.sin(q1+q2)-math.sin(q1), -math.sin(q1+q2), 0],
        [math.cos(q1+q2) + math.cos(q1), math.cos(q1+q2), 0],
        [0, 0, 1],
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 0]]
    fk = np.dot(J,vel)
    print("End Effector Velocity: \n", fk)
    
def vfk_service():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'vfk_service' node so that multiple vfk_services can
    # run simultaneously.
    rospy.init_node('vfk_service', anonymous=True)

    rospy.Subscriber("/rrbot/joint_states", JointState, callback)
    print("service worked")

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    vfk_service()
