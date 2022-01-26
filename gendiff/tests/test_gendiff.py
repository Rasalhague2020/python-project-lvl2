import pytest

import os

from gendiff import generator


def get_full_file_path(filename):
    return os.path.join(
        os.getcwd(), 'gendiff', 'tests', 'fixtures', filename
    )


@pytest.fixture
def right_diff():
    filename = 'right_answer.txt'
    path = get_full_file_path(filename)

    with open(path, 'r') as file:
        test_diff = ''
        for line in file:
            test_diff += line
    return test_diff


def test_generator(right_diff):
    json_first_file = 'file1.json'
    json_second_file = 'file2.json'

    path_1 = get_full_file_path(json_first_file)
    path_2 = get_full_file_path(json_second_file)

    assert right_diff == generator.generate_diff(path_1, path_2)

    yaml_first_file = 'file1.yml'
    yaml_second_file = 'file2.yml'

    path_1 = get_full_file_path(yaml_first_file)
    path_2 = get_full_file_path(yaml_second_file)

    assert right_diff == generator.generate_diff(path_1, path_2)
