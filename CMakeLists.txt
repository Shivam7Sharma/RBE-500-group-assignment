cmake_minimum_required(VERSION 3.0.2)
project(forward_kinematics_ros)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  sensor_msgs
  message_generation
)

## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   Num.msg
 )
 
 add_message_files(DIRECTORY msg FILES Num.msg)
 add_service_files(DIRECTORY srv FILES ForwardKinematics.srv)

## Generate services in the 'srv' folder
 add_service_files(
   FILES
   ForwardKinematics.srv
   inverse_kinematics_.srv
 )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   std_msgs
   sensor_msgs
)


catkin_package(CATKIN_DEPENDS message_runtime)

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if your package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also needS
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES beginner_tutorials
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


add_executable(forward_kinematics_server src/forward_kinematics_server.cpp)
target_link_libraries(forward_kinematics_server ${catkin_LIBRARIES})
add_dependencies(forward_kinematics_server forward_kinematics_ros_gencpp)

add_executable(forward_kinematics_client src/forward_kinematics_client.cpp)
target_link_libraries(forward_kinematics_client ${catkin_LIBRARIES})
add_dependencies(forward_kinematics_client forward_kinematics_ros_gencpp)

add_executable(listener src/listener.cpp)
target_link_libraries(listener ${catkin_LIBRARIES})
add_dependencies(listener forward_kinematics_ros_gencpp)

add_executable(forward_kinematics src/forward_kinematics.cpp)
target_link_libraries(forward_kinematics ${catkin_LIBRARIES})
add_dependencies(forward_kinematics forward_kinematics_ros_gencpp)


catkin_install_python(PROGRAMS scripts/inverse_kinematics_server.py scripts/inverse_kinematics_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
