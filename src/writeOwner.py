import os
import numpy as np



def writeOwner(field_array, totalNumberOfFaces):
	fileWrite = open("constant/polyMesh/owner","wb")
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
	'    class       labelList;\n'
	'    location    "constant/polyMesh";\n'
	'    object      owner;\n'
	'}\n'
	'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n\n'.encode('ascii'))



	fileWrite.write(str(totalNumberOfFaces).encode('ascii'))
	fileWrite.write('\n(\n'.encode('ascii'))

	for i in field_array:	

		fileWrite.write(str(i).encode('ascii'))
		fileWrite.write('\n'.encode('ascii'))
		
	fileWrite.write(')\n'.encode('ascii'))
	
	fileWrite.write('// ************************************************************************* //\n'.encode('ascii'))
	fileWrite.close()
