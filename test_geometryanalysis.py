
"""
Tests for geometryanalysis.py (write a note about what this is)
file must start with the word test
run pytest in terminal and any file in that directory with test in the beginning will be tested.


pytest -v to list out each function check

"""

import geometryanalysis as ga
import pytest

def test_calculate_distance():
    coord1 = [0, 0, 2]
    coord2 = [0, 0, 0]

    observed = ga.calculate_distance(coord1, coord2)

    assert observed == 2


def test_bond_check_false():
    bond_distance = 3.0


    observed = ga.bond_check(bond_distance)

    assert observed == False



def test_bond_check_true():
    bond_distance = 1.0


    observed = ga.bond_check(bond_distance)

    assert observed == True

def test_bond_check_error():
    bond_distance = 'a'

    with pytest.raises(TypeError):
        observed = ga.bond_check(bond_distance)