cmake_minimum_required(VERSION 2.8.3)
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

  install(PROGRAMS
      nodes/example_node
      DESTINATION lib/${PROJECT_NAME}
  )

endif()

