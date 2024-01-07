
import os
import numpy as np




def writeT(output):
	# Get the data array
	data_array = output.GetCellData().GetArray("TMean")  # Change "p" to the actual field name




	# Convert the data to a NumPy array

	field_array = np.array([data_array.GetTuple1(i) for i in range(data_array.GetNumberOfTuples())])



	fileWrite = open("0/T","wb")
	fileWrite.write('/*--------------------------------*- C++ -*----------------------------------*\\\n'
	'| =========                 |                                                 |\n'
	'| \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n'
	'|  \\\\    /   O peration     | Version:  2306                                  |\n'
	'|   \\\\  /    A nd           | Website:  www.openfoam.com                      |\n'
	'|    \\\\/     M anipulation  |                                                 |\n'
	'\*---------------------------------------------------------------------------*/\n'
	'FoamFile\n'
	'{\n'
	'    version     2.0;\n'
	'    format      ascii;\n'
	'    arch        "LSB;label=32;scalar=64";\n'
	'    class       volScalarField;\n'
	'    location    "527";\n'
	'    object      T;\n'
	'}\n'
	'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n\n'

	'dimensions      [0 0 0 1 0 0 0];\n\n'

	'internalField   nonuniform List<scalar>\n'.encode('ascii'))
	fileWrite.write(str(np.shape(field_array)[0]).encode('ascii'))
	fileWrite.write('\n(\n'.encode('ascii'))
	sum = 0
	for i in field_array:	
		sum = sum + 1;
	#	if sum ==89870:
	#		fileWrite.write('\n'.encode('ascii'))
	#		break
		fileWrite.write(str(i)[0:-1].encode('ascii'))

		fileWrite.write('\n'.encode('ascii'))
	fileWrite.write(')\n'.encode('ascii'))
	fileWrite.write(';\n'.encode('ascii'))
	fileWrite.write('boundaryField\n'.encode('ascii'))
	fileWrite.write('{\n'.encode('ascii'))
	fileWrite.write('\t\t}\n'.encode('ascii'))
	fileWrite.write('\tnewWing\n'.encode('ascii'))
	fileWrite.write('\t{\n'.encode('ascii'))
	fileWrite.write('\t\ttype\t\t\tempty\n;'.encode('ascii'))
	fileWrite.write('\t}\n'.encode('ascii'))
	fileWrite.write('// ************************************************************************* //\n'.encode('ascii'))
	fileWrite.close()
