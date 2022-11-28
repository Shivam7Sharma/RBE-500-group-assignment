# RBE-500-group-assignment
This group assigment had three parts and this repository has the code for all the three parts.



RBE 500 – Group Assignment – Part 1   

1) Create the robot: Create the SCARA robot in ROS and Gazebo.  
 
2) Forward Kinematics:  Implement a forward kinematics node
 
3) Inverse Kinematics: Implement an inverse kinematics node (a separate node) that has a 
service client that takes a (desired) pose of the end effector and returns joint positions as a 
response.

Part 2 :
 
This assignment is about controlling the robot joints.  
 
1) Implement a position controller for your robot. You can do this in two ways 
a. You can write your own node that gets the joint positions from Gazebo, implements a 
PD controller and sends joint efforts or 
b. You can use the ros_control package that will provide you the controllers. Please see the 
tutorial: http://gazebosim.org/tutorials/?tut=ros_control 
2) In either case, you will need to tune the PD gains (you do not need to calculate them in this 
assignment). Do your best to have fast convergence with minimal overshoot. (While doing so, 
you may want to first fix the all the joints except the last joint by changing the joint type field of 
the corresponding joints to “fixed”. Tune it for that joint and move to the next ones. You do not 
have to do the tuning this way; it is just a suggestion.)  
3) Record the reference positions and current positions of the joints in a text file and plot them via 
Matlab with respect to time to present the response of your system to ‘step’ references.

Part 3:

This assignment is about moving the robot on a linear path. 
 
1) (4 pts) Velocity Level Kinematics: Implement a node with two services. One takes joint velocities 
and converts them to end effector velocities, and the second one takes end effector velocities 
and converts them to joint velocities. 
2) (2 pts) Using the position controllers in Part 2, move the robot to a position that is significantly 
away from singular configurations. 
3) (2.5 pts) Write velocity controllers for all the joints (again you can either use ros_control 
packages or implement your own).  
4) (1.5) Give a constant velocity reference in the positive ‘y’ direction of the Cartesian space. 
Convert this velocity to the joint space using your Jacobian and feed it as a reference to your 
velocity controllers. This should make the robot move on a straight line in the +y direction. 
Record the generated velocity references together with the actual velocity of the system over 
time, and plot via Matlab. 
