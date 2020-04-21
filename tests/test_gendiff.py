from gendiff import generate_diff


def test_diff():
    with open('./tests/fixtures/correct_out1.txt', 'r') as f:
        assert (f.read() ==
                generate_diff('./tests/fixtures/before.json',
                              './tests/fixtures/after.json'))
