cmake_minimum_required(VERSION 3.14)
project(HentaiFetch)

add_subdirectory(Dependencies/SugarHTTPS)

file(GLOB MAIN_SOURCES
    ${CMAKE_SOURCE_DIR}/Source/*.cpp
)

add_executable(Main ${MAIN_SOURCES})

target_include_directories(Main PUBLIC 
    ${CMAKE_SOURCE_DIR}/Include/
)

target_link_libraries(Main SugarHTTPS)

set_target_properties(Main PROPERTIES
    CMAKE_CXX_STANDARD 20
    CMAKE_CXX_STANDARD_REQUIRED TRUE
)
