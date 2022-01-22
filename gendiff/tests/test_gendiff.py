import pytest

import os

from gendiff import generator

@pytest.fixture
def right_diff():
    filename = 'right_answer.txt'
    path = os.path.join(os.getcwd(), 'gendiff', 'tests', filename)

    with open(path, 'r') as file:
        test_diff = ''
        for line in file:
            test_diff += line 
    return test_diff


def test_generator(right_diff):
    filename_1 = 'file1.json'
    filename_2 = 'file2.json'

    path_1 = os.path.join(os.getcwd(), 'gendiff', 'tests', filename_1)
    path_2 = os.path.join(os.getcwd(), 'gendiff', 'tests', filename_2)
    # print('--', path_1)
    # print('--', path_2)
    # print('g-', generator.generate_diff(path_1, path_2))
    # print('r-', right_diff)
    assert right_diff == generator.generate_diff(path_1, path_2)
