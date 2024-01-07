import numpy as np
import os





def writeU(output):

	data_array = output.GetCellData().GetArray("UMean")
	# Convert the data to a NumPy array
	import numpy as np
	field_array = np.array([data_array.GetTuple3(i) for i in range(data_array.GetNumberOfTuples())])


	fileWrite = open("0/U","wb+")

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
	'    class       volVectorField;\n'
	'    location    "527";\n'
	'    object      U;\n'
	'}\n'
	'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n\n'

	'dimensions      [0 1 -1 0 0 0 0];\n\n'

	'internalField   nonuniform List<vector>\n'.encode('ascii'))
	fileWrite.write(str(np.shape(field_array)[0]).encode('ascii'))




	fileWrite.write('\n(\n'.encode('ascii'))
	for i in field_array:	
		fileWrite.write('('.encode('ascii'))
		fileWrite.write(str(i)[1:-1].encode('ascii'))
	#	fileWrite.write(bytearray(i, 'utf_16'))
		fileWrite.write(')\n'.encode('ascii'))
	fileWrite.write(')\n'.encode('ascii'))
	fileWrite.write(';\n'.encode('ascii'))

	fileWrite.write('boundaryField\n'.encode('ascii'))
	fileWrite.write('{\n'.encode('ascii'))
	fileWrite.write('\t\t}\n'.encode('ascii'))
	fileWrite.write('\tnewWing\n'.encode('ascii'))
	fileWrite.write('\t{\n'.encode('ascii'))
	fileWrite.write('\t\ttype\t\t\tempty;\n'.encode('ascii'))
	fileWrite.write('\t}\n'.encode('ascii'))
	fileWrite.write('// ************************************************************************* //\n'.encode('ascii'))



	fileWrite.close()

