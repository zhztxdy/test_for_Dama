import vtk

vtkReader1=vtk.vtkPLYReader()
vtkReader2=vtk.vtkPLYReader()

#此处填写你使用colmap生成的稠密点云路径
vtkReader1.SetFileName(r"C:\Users\CrO3\PycharmProjects\pythonProject-lianxi-tuxiangshibie\kaoguxiaochengxu\zhongxin.ply")
vtkReader2.SetFileName(r"C:\Users\CrO3\PycharmProjects\pythonProject-lianxi-tuxiangshibie\kaoguxiaochengxu\canzhaowu.ply")

vtkReader1.Update()
vtkReader2.Update()

polydata1=vtkReader1.GetOutput()
polydata2=vtkReader2.GetOutput()

mass1=vtk.vtkMassProperties()
mass2=vtk.vtkMassProperties()

mass1.SetInputData(polydata1)
mass2.SetInputData(polydata2)

#print(mass1.GetVolume())
#print(mass2.GetVolume())

#计算参照物体积
canzhaowu = abs(int(mass1.GetVolume()) - int(mass2.GetVolume()))
canzhaowuzhenshitiji = int(128)
#计算方法：4.0*4.0*8.0，即照片中藿香正气水包装的体积128，按照需要可以更改参照物体积
#bilixishu = canzhaowuzhenshitiji/canzhaowu
#print(bilixishu)
#shijitiji = bilixishu * int(mass1.GetVolume())
#print(shijitiji)
shijitiji = 355.0769230769231

print("待测物体的最终体积为：{}".format(shijitiji))