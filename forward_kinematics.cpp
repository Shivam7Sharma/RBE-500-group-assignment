#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Float64.h"
#include "sensor_msgs/JointState.h"
#include <iostream>
#include <sstream>
using namespace std;
#include "math.h"  

float q1, q2, q3;
float cosine, sine;
float c12, s12; 
float transform_matrix[4][4];

float l1 = 1;
float l2 = 1;

void chatterCallback(const sensor_msgs::JointState::ConstPtr &msg)
{
     float q1=msg->position[0];
     float q2=msg->position[1];
     float q3=msg->position[2];
}


int main(int argc, char **argv)
{
  ros::init(argc, argv, "talker");
  ros::NodeHandle n;
  ros::Publisher chatter_pub = n.advertise<std_msgs::Float64>("forward_kinematics", 1000);
  ros::Rate loop_rate(10);

  while (ros::ok())
  {
    cosine = cos(q1);
    sine = sin(q1);
    c12 = cos(q1 + q2);
    s12 = sin(q1 + q2);

    float transform_matrix[4][4] = {{c12, -1*s12, 0, l2*c12 + l2*cosine}, {s12, c12, 0, l2*s12 + l2*sine}, {0, 0, 1, q3+l1}, {0, 0, 0, 1}};
    
    std_msgs::Float64 x;
    std_msgs::Float64 y;
    std_msgs::Float64 z;

    //x, y, and z values in the matrix
    x.data = transform_matrix[0][3];
    y.data = transform_matrix[1][3];
    z.data = transform_matrix[2][3];

    //Message publised with talker
    ROS_INFO("Calculating forward kinematics");

    //x, y, and z values published to topic
    chatter_pub.publish(x);
    chatter_pub.publish(y);
    chatter_pub.publish(z);

    ros::spinOnce();

    loop_rate.sleep();

  }

  return 0;
}
