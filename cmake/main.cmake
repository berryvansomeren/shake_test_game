#----------------------------------------------------------------
# The libshake project contains the shake executable

# Create project
set( PROJECT_NAME shake_test_game )
project( ${PROJECT_NAME} VERSION 0.0.1 LANGUAGES CXX )

file( GLOB_RECURSE
    PYTHON_FILES
    content/*.py
    content/dummy.hpp
    content/dummy.cpp
)

add_executable( game1 ${PYTHON_FILES} )