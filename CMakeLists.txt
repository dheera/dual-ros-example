cmake_minimum_required(VERSION 3.5)
project(dual_ros_example)

macro(print_all_variables)
    message(STATUS "print_all_variables------------------------------------------{")
    get_cmake_property(_variableNames VARIABLES)
    foreach (_variableName ${_variableNames})
        message(STATUS "${_variableName}=${${_variableName}}")
    endforeach()
    message(STATUS "print_all_variables------------------------------------------}")
endmacro()

# print_all_variables()

if(DEFINED CATKIN_ENV)
  # ROS1
  message("ROS1 install")

  find_package(catkin REQUIRED COMPONENTS
    rospy
    std_msgs
    sensor_msgs
  )

  catkin_python_setup()
  catkin_package()

  include_directories(
    ${catkin_INCLUDE_DIRS}
  )

  catkin_install_python(PROGRAMS
    nodes/example_node
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  )

else()
  # ROS2
  message("ROS2 install")

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

ament_python_install_package("dual_ros_example")

  install(PROGRAMS
      nodes/example_node
      DESTINATION lib/${PROJECT_NAME}
  )

  ament_package()

endif()

