#!/usr/bin/env python
# *-* coding:utf-8 *-*

from vtk import *


#读取，使用的是vtkMetaImageReader类读取MHD格式
file_name = r"G:\graduate project\VolumeRenderData\backpack8.raw\backpack8.mhd"
reader = vtkMetaImageReader()
reader.SetFileName(file_name)

#vtkImageCast进行数据类型转换，这里转换成unsignedShort
cast = vtkImageCast()
cast.SetInputConnection(reader.GetOutputPort())
cast.SetOutputScalarTypeToUnsignedShort()
cast.Update()
output = cast.GetOutputPort()

'''
#或者使用vtk格式直接读取
file_name = r"mummy.128.vtk"
reader = vtkStructuredPointsReader()
reader.SetFileName(file_name)
reader.Update()
output = reader.GetOutputPort()
'''

#定义体绘制算法函数
rayCastFun = vtkVolumeRayCastCompositeFunction()  #光线投射法
##rayCastFun = vtkVolumeRayCastMIPFunction() #最大密度法
##rayCastFun = vtkVolumeRayCastIsosurfaceFunction()  #特定等值面法

#设置体绘制的Mapper，有两个输入
volumeMapper = vtkVolumeRayCastMapper()
volumeMapper.SetInputConnection(output) #第一个是输入图像数据
volumeMapper.SetVolumeRayCastFunction(rayCastFun)  #另一个是设置体绘制的光线投射函数


#########接下来到了设置体绘制的各种属性的时间www############################
'''
#设置光线采样距离
volumeMapper.SetSampleDistance(volumeMapper.GetSampleDistance()*4)
#设置图像采样步长
volumeMapper.SetAutoAdjustSampleDistances(0)
volumeMapper.SetImageSampleDistance(4)
'''
#体绘制属性设置
volumeProperty = vtkVolumeProperty()
volumeProperty.SetInterpolationTypeToLinear()
volumeProperty.ShadeOn() #打开或者关闭阴影测试
volumeProperty.SetAmbient(0.4)
volumeProperty.SetDiffuse(0.6)
volumeProperty.SetSpecular(0.2)

#灰色不透明函数
compositeOpacity = vtkPiecewiseFunction()
compositeOpacity.AddPoint(70, 0.00)
compositeOpacity.AddPoint(90, 0.40)
compositeOpacity.AddPoint(180, 0.60)
volumeProperty.SetScalarOpacity(compositeOpacity) #灰色不透明函数导入体绘制属性

#颜色传输函数
color = vtkColorTransferFunction()
color.AddRGBPoint(0.000,  0.00, 0.00, 0.00)
color.AddRGBPoint(64.00,  1.00, 0.52, 0.30)
color.AddRGBPoint(190.0,  1.00, 1.00, 1.00)
color.AddRGBPoint(220.0,  0.20, 0.20, 0.20)
volumeProperty.SetColor(color) #导入颜色函数

#梯度不透明函数
volumeGradientOpacity = vtkPiecewiseFunction()
volumeGradientOpacity.AddPoint(10, 0.0)
volumeGradientOpacity.AddPoint(90, 0.5)
volumeGradientOpacity.AddPoint(110, 1.0)
##volumeProperty.SetGradientOpacity(volumeGradientOpacity)#导入梯度不透明效果

#vtkVolume类型，相似于vtkActor，接受两个输入
volume = vtkVolume()
volume.SetMapper(volumeMapper) #设置Mapper对象
volume.SetProperty(volumeProperty) #设置属性对象


######################################渲染引擎设置############################

ren = vtkRenderer()
ren.SetBackground(1.0, 1.0, 1.0)
ren.AddVolume(volume)

renWin = vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.Render()
renWin.SetWindowName("VolumeRenderingApp")

iren = vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
ren.ResetCamera()

renWin.Render()
iren.Start()






