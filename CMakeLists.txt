cmake_minimum_required (VERSION 3.10)
project(incppect)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(CMAKE_EXPORT_COMPILE_COMMANDS "on")

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

option(INCPPECT_DEBUG   "Enable debug messages in the incppect service" ON)
option(INCPPECT_NO_SSL  "Disable SSL support" OFF)

find_package(Threads REQUIRED)
add_subdirectory(src)

if (CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
    add_subdirectory(examples)
endif ()
