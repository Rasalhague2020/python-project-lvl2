import pytest


@pytest.fixture
def right_diff():
    test_diff = "{\n- follow: false\nhost: hexlet.io\n\
    - proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n\
    + verbose: true\n}"
    return test_diff


def test_generator(right_diff):
    assert right_diff == "123"