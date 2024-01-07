
import os
import numpy as np




def writePoints(output):
	Points = output.GetPoints()  # Change "p" to the actual field name
	num_points = Points.GetNumberOfPoints()




	# Convert the data to a NumPy array

	field_array = np.array([Points.GetPoint(i) for i in range(num_points)])

	fileWrite = open("constant/polyMesh/points","wb")



	fileWrite.write('/*--------------------------------*- C++ -*----------------------------------*\\\n'
	'| =========                 |                                                 |\n'
	'| \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n'
	'|  \\\\    /   O peration     | Version:  2306                                  |\n'
	'|   \\\\  /    A nd           | Website:  www.openfoam.com                      |\n'
	'|    \\\\/     M anipulation  |                                                 |\n'
	'\*---------------------------------------------------------------------------*/\n'
	'FoamFile\n'
	'{\n'
	'    format      ascii;\n'
	'    class       vectorField;\n'
	'    location    "constant/polyMesh";\n'
	'    object      points;\n'
	'}\n'
	'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n\n\n'.encode('ascii'))

	fileWrite.write(str(np.shape(field_array)[0]).encode('ascii'))

	fileWrite.write('\n(\n'.encode('ascii'))
	sum = 0
	for i in field_array:	
		sum = sum + 1;
		fileWrite.write('('.encode('ascii'))
		fileWrite.write(str(i)[1:-1].encode('ascii'))
	#	fileWrite.write(bytearray(i, 'utf_16'))
		fileWrite.write(')\n'.encode('ascii'))
	fileWrite.write(')\n'.encode('ascii'))
	fileWrite.write(';\n\n\n'.encode('ascii'))


	fileWrite.write('// ************************************************************************* //\n'.encode('ascii'))
	fileWrite.close()



