import vtk
import os
import shutil
import numpy as np
from writeFace import writeFace
from writeOwner import writeOwner
from writeNeighbour import writeNeighbour
from writeU import writeU
from writePoints import writePoints
from writeT import writeT
from PyFoam.Execution.BasicRunner import BasicRunner
import subprocess



# Specify the path to your VTK file
vtk_file_path = 'internal.vtu'

# Read the VTK file
reader = vtk.vtkXMLUnstructuredGridReader()
reader.SetFileName(vtk_file_path)
reader.Update()

# Get the data array




output = reader.GetOutput()  # Change "p" to the actual field name
num_cells = output.GetNumberOfCells()
#print(output.GetNumberOfFaces())
field_array = []
owner = []
field_array_for_sorting = []

for i in range(num_cells):
	for j in range(output.GetCell(i).GetNumberOfFaces()):
		facePoints = [output.GetCell(i).GetFace(j).GetPointId(l) for l in range(output.GetCell(i).GetFace(j).GetNumberOfPoints())]
		field_array.append(facePoints[:])		
		field_array_for_sorting.append(np.sort(facePoints[:4]))
		owner.append(i)

num_raw_ele = np.shape(field_array_for_sorting)
_, idx, revidx = np.unique(field_array_for_sorting, axis = 0, return_index=True, return_inverse=True)

neighbourIdx = []
for k in range(num_raw_ele[0]):
	if k not in idx:
		neighbourIdx.append(np.where(revidx[k] == revidx))
owner = np.array(owner)
neighbourIdx = np.array(neighbourIdx).reshape(-1,2)
indexToMoveInternalFaces = np.array(list(neighbourIdx[:,0]) + list(idx))
_, indexToUniqueFaces = np.unique(indexToMoveInternalFaces, return_index=True)
Idx = [indexToMoveInternalFaces[indx] for indx in sorted(indexToUniqueFaces)]
neighbour_array = owner[neighbourIdx]
owner_array = owner[Idx]
face_array = [field_array[arr] for arr in Idx]
writeFace(face_array, np.shape(Idx)[0])
writeOwner(owner_array, np.shape(Idx)[0])
writeNeighbour(neighbour_array, np.shape(neighbour_array)[0])
writeU(output)
writePoints(output)
writeT(output)

# mapping to blockMesh

mapFieldDir = 'mapfield'
#os.chdir(os.path.dirname(os.getcwd()))
os.chdir(mapFieldDir)
shutil.rmtree('0')
shutil.copytree('0file/0', './0')

#openfoam_installation_path = '/usr/lib/openfoam/openfoam2306'
#/usr/lib/openfoam/openfoam2306/applications/utilities/mapFields

# Source and target case directories
path = os.getcwd()
source_case = os.path.dirname(path)
target_case = path

map_fields_runner = BasicRunner(
    argv=["mapFields", "-sourceTime", "latestTime", "-case", target_case, source_case], silent=True, logname="mapFields"
)

map_fields_runner.start()


foamToVTK = BasicRunner(
        argv=["foamToVTK", "-latestTime", "-no-boundary", "-fields",
              "'(T U)'",
              "-overwrite", "-name", 'vtkfile'], silent=True, logname="foamToVTK")
foamToVTK.start()

os.chdir(source_case)
shutil.move('mapfield/vtkfile', 'Database')


subprocess.run(["rm", "-f", "foamToVTK.logfile"])
subprocess.run(["rm", "-f", "mapFields.logfile"])
subprocess.run(["rm", "-f", "mapfields.foam"])


