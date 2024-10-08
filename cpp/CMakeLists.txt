cmake_minimum_required(VERSION 3.14)


project(precompiled)


set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# include dir
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/precompiled)


# set lib
add_library(precompiled STATIC
    precompiled/ListNode.cpp
    precompiled/TreeNode.cpp
    precompiled/NestedInteger.cpp
)

# set install dir
install(TARGETS precompiled
    EXPORT precompiledTargets
    ARCHIVE DESTINATION lib
)

# install
install(FILES
    precompiled/headers.h
    precompiled/ListNode.h
    precompiled/TreeNode.h
    precompiled/NestedInteger.h
    DESTINATION include/precompiled
)

