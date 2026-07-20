cmake_minimum_required(VERSION 3.8)
project(bci_hand_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY urdf config launch
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_cmake_pytest REQUIRED)
  ament_add_pytest_test(test_hand_description test/test_hand_description.py)
endif()

ament_package()
