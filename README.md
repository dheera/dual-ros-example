# Dual ROS1/ROS2 package

This is an example of a ROS package that should work in either ROS1 or ROS2.

## ROS 1 example

```
source /opt/ros/noetic/setup.bash
mkdir -p catkin_ws/src/
cd catkin_ws/src/
catkin_init_workspace
git clone https://github.com/dheera/dual-ros-example
cd ..
catkin_make
source devel/setup.bash
rosrun dual_ros_example example_node
```

## ROS 2 example

```
source /opt/ros/foxy/setup.bash
mkdir -p colcon_ws/src/
cd colcon_ws/src/
git clone https://github.com/dheera/dual-ros-example
cd ..
colcon build
source install/setup.bash
ros2 run dual_ros_example example_node
```
