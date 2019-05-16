#!/usr/bin/env python


import numpy
import os
import sys

def calculate_distance(atom1, atom2):
    """
    calculate the distance btwn two atoms. This is a doc string

    explain what the function does but not how it does it. Dashes have to be exactly as long as the word.

    Parameters
    ----------
    atom1: list
        longer explanation of atom1. A list of coordinates [x, y, z].
    atom2: list
        list of coordinates [x, y, z].

    Returns
    -------
    bond_lengths: float
        The distance between atoms.

    Examples
    --------
    >> calculate_distance([0,0,0],[0,0,1])
    1.0

    """
    x_dist = atom1[0] - atom2[0]
    y_dist = atom1[1] - atom2[1]
    z_dist = atom1[2] - atom2[2]
    distance = numpy.sqrt(x_dist**2 + y_dist**2 + z_dist**2)
    return distance



def bond_check(bond_distance, minimum_value=0, maximum_value=1.5): # min and max values = x, where x is the default value if not specified in the cell below.
    """
    This function checks if the distance between two atoms is within a min and max distance.

    Parameters
    ----------
    bond_distance:  float
        The distance between two atoms
    minimum_value: float
        The minimum distance between two atoms
    maximum_value:
        The max distance between two atoms

    Returns
    -------
    True if bond
    False if not a bond

    """



    if bond_distance > minimum_value and bond_distance < maximum_value:
        return True
    else:
        return False

    if not isinstance(atom_distance, float):
        raise TypeError(F'atom_distance must be type float. {atom_distance}')


def open_xyz(filename):
    xyz_file = np.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coord = (xyz_file[:,1:])
    coord = coord.astype(np.float)
    return(symbols, coord)



if __name__ == "__main__":


    if len(sys.argv) < 2:
        raise IndexError('No file name given. Script requires an xyz file')

    xyzfilename = sys.argv[1]

    symbols, coord = open_xyz(xyzfilename)

    for numA, atomA in enumerate(coordinates):
        for numB, atomB in enumerate(coordinates):
            if numB < numA:
                distance_AB = calculate_distance(atomA, atomB)
                if bond_check(distance_AB, maximum_value=2.0): #if you dont want the default, you only need to specify the value you want to change. (here, maximum_value is changed to 2.0)
                    print(F'{symbols[numA]} to {symbols[numB]}: {distance_AB:.3f}')











