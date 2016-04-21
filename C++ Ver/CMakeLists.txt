#**********************************************************************


CMAKE_MINIMUM_REQUIRED(VERSION 2.6)
PROJECT(vtkVolumeRender)
 
FIND_PACKAGE(VTK REQUIRED)
INCLUDE(${VTK_USE_FILE})
 
ADD_EXECUTABLE(7.1_VolumeRenderingApp 7.1_VolumeRenderingApp.cpp)
TARGET_LINK_LIBRARIES(7.1_VolumeRenderingApp ${VTK_LIBRARIES})



#-----------------------------------------------------------------------------------------------------------------------------------
# Construct a list of paths containing runtime directories for project applications on Windows.
# Create two batch files which correctly set up the environment for the application and for Visual Studio.
IF(WIN32)
  SET(PROJECT_RUNTIME_PATH "${VTK_DIR}/bin/@VS_BUILD_TYPE@")
  INCLUDE(CreateWindowsBatchScript.cmake)
  SET(VS_SOLUTION_FILE "${PROJECT_BINARY_DIR}/${PROJECT_NAME}.sln")
  FOREACH(VS_BUILD_TYPE Debug Release)
    CreateWindowsBatchScript("${CMAKE_SOURCE_DIR}/StartVS.bat.in"
      ${PROJECT_BINARY_DIR}/StartVS_${VS_BUILD_TYPE}.bat
      ${VS_BUILD_TYPE})
  ENDFOREACH()
ENDIF(WIN32)
