from gendiff import generate_diff


def test_diff():
    with open('./tests/fixtures/correct_out1.txt', 'r') as f:
        correct_out = f.read()
    assert (correct_out ==
            generate_diff('./tests/fixtures/before.json',
                          './tests/fixtures/after.json'))
    assert (correct_out ==
            generate_diff('./tests/fixtures/before.yml',
                          './tests/fixtures/after.yml'))
