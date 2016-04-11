from vtk import *
 
# The source file
file_name = "head.vtk"
 
# Read the source file.
reader = vtkStructuredPointsReader()
reader.SetFileName(file_name)

marchingCubes = vtkMarchingCubes()
marchingCubes.SetInputConnection(reader.GetOutputPort())
marchingCubes.SetValue(0, 500)

# Create the mapper that corresponds the objects of the vtk file
# into graphics elements
mapper = vtkPolyDataMapper()
mapper.SetInputConnection(marchingCubes.GetOutputPort())

 
# Create the Actor
actor = vtkActor()
actor.SetMapper(mapper)
 
# Create the Renderer
renderer = vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(1.0, 1.0, 1.0) # Set background to white
 
# Create the RendererWindow
renWin = vtkRenderWindow()
renWin.AddRenderer(renderer)
renWin.Render()
renWin.SetWindowName("vtkPipeLineDemo")
 
# Create the RendererWindowInteractor and display the vtk_file
interactor = vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWin)


interactor.Initialize()
interactor.Start()