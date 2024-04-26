cmake_minimum_required(VERSION 3.5)
project(cpp)

set(CMAKE_CXX_STANDARD 14)

find_package(OpenMP REQUIRED)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/build)

set(SOURCE_FILES main.cpp io.cpp kmb.cpp dijkstra.cpp prim_mst.cpp graph.cpp edge.cpp kmb_sequential.cpp kmb_both_parallel.cpp kmb_outer_parallel.cpp kmb_inner_parallel.cpp)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")

add_executable(kmb ${SOURCE_FILES})

set(SOURCE_FILES original_2approx_kmb_cpu.cpp)
add_executable(og ${SOURCE_FILES})

target_link_libraries(kmb PUBLIC OpenMP::OpenMP_CXX)
