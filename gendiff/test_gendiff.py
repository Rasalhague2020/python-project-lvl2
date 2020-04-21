from gendiff import engine


def test_diff():
    with open('./gendiff/tests/fixtures/correct_out1.txt', 'r') as f:
        assert (f.read() ==
                engine.generate_diff('./gendiff/tests/fixtures/before.json',
                                     './gendiff/tests/fixtures/after.json'))
