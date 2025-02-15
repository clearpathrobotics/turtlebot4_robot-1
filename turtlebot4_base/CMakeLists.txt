cmake_minimum_required(VERSION 3.5)
project(turtlebot4_base)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(rcutils REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(irobot_create_msgs REQUIRED)
find_package(turtlebot4_msgs REQUIRED)
find_package(turtlebot4_node REQUIRED)

find_library(GPIOD_LIBRARY NAMES libgpiod.so)

#Build

include_directories(
  include
)

add_library(${PROJECT_NAME}_lib
  "src/main.cpp"
  "src/turtlebot4.cpp"
  "src/display.cpp"
  "src/ssd1306.cpp"
  "src/ssd1306_fonts.cpp"
  "src/i2c_interface.cpp"
  "src/gpio_interface.cpp"
  "src/buttons.cpp"
  "src/leds.cpp"
)

set(DEPENDENCIES
  "rclcpp"
  "rclcpp_action"
  "rcutils"
  "std_msgs"
  "sensor_msgs"
  "irobot_create_msgs"
  "turtlebot4_msgs"
  "turtlebot4_node"
)

target_link_libraries(${PROJECT_NAME}_lib ${GPIOD_LIBRARY})

ament_target_dependencies(${PROJECT_NAME}_lib ${DEPENDENCIES})

set(EXECUTABLE_NAME "turtlebot4_base_node")

add_executable(${EXECUTABLE_NAME} src/main.cpp)
target_link_libraries(${EXECUTABLE_NAME} ${PROJECT_NAME}_lib)
ament_target_dependencies(${EXECUTABLE_NAME} ${DEPENDENCIES})

install(TARGETS ${EXECUTABLE_NAME}
  DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  list(APPEND AMENT_LINT_AUTO_EXCLUDE
    ament_cmake_copyright
  )
  ament_lint_auto_find_test_dependencies()
endif()


ament_export_include_directories(include)
ament_package()
