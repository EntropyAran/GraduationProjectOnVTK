#!/usr/bin/env python
# *-* coding:utf-8 *-*

#这段代码用于演示如何创造简单的vtk对象然后使用渲染

import vtk
# 导入使用的颜色
from vtk.util.colors import tomato

# vtkCylinder类用于创建柱体的实例，并且可以对实例后的对象设置各种参数
cylinder = vtk.vtkCylinderSource()
cylinder.SetResolution(8)
##cylinder.SetHeight(1.0)

# 该类用于对多边形几何数据转化为几何图元进行渲染
cylinderMapper = vtk.vtkPolyDataMapper()
cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

# 用于将几何渲染之后的数据进行可视化渲染，并且还可设置可视化时的参数
cylinderActor = vtk.vtkActor()
cylinderActor.SetMapper(cylinderMapper)
cylinderActor.GetProperty().SetColor(tomato)
##cylinderActor.RotateX(30.0)
##cylinderActor.RotateY(-45.0)

# vtkRender类用于场景渲染
# vtkRenderWindow用于和使用的平台进行渲染引擎的连接
# vtkRenderWindowInteractor则是平台独立的交互机制
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# 将多边形渲染导入场景渲染器，并设置场景和窗口的初始参数
ren.AddActor(cylinderActor)
ren.SetBackground(0.1, 0.2, 0.4)
renWin.SetSize(200, 200)

# 普通的鼠标交互控件
style = vtk.vtkInteractorStyleTrackballCamera()
iren.SetInteractorStyle(style)


# 这一段用于设置照明，一共两个，蓝色和绿色
myLight = vtk.vtkLight()
myLight.SetColor(0, 1,0)
myLight.SetPosition(0, 0, 1)
myLight.SetFocalPoint(ren.GetActiveCamera().GetFocalPoint())
ren.AddLight(myLight)

myLight2 = vtk.vtkLight()
myLight2.SetColor(0, 0, 1)
myLight2.SetPosition(0, 0, -1)
myLight2.SetFocalPoint(ren.GetActiveCamera().GetFocalPoint())
ren.AddLight(myLight2)


# 开始进行可视化的开始
iren.Initialize()

# 初始相机，开始窗口渲染
ren.ResetCamera()
ren.GetActiveCamera().Zoom(1.5)
renWin.Render()

# 整个程序渲染开始
iren.Start()
