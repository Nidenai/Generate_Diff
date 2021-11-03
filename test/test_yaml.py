from gendiff.engine.differ import generate_diff


def test_base():
    file_for_read = open('test/fixtures/test_diff_json.txt')
    path_one = 'test/fixtures/examples/file1.yaml'
    path_two = 'test/fixtures/examples/file2.yaml'
    result = file_for_read.read()
    test_result = generate_diff(path_one, path_two)
    assert result == test_result


def test_rec():
    file_for_read = open('test/fixtures/test_diff_json_rec.txt')
    path_one = 'test/fixtures/examples/file1_rec.yaml'
    path_two = 'test/fixtures/examples/file2_rec.yaml'
    result = file_for_read.read()
    test_result = generate_diff(path_one, path_two)
    assert result == test_result


def test_plain():
    file_for_read = open('test/fixtures/test_diff_json_plain.txt')
    path_one = 'test/fixtures/examples/file1_rec.yaml'
    path_two = 'test/fixtures/examples/file2_rec.yaml'
    result = file_for_read.read()
    test_result = generate_diff(path_one, path_two, format_name='plain')
    assert result == test_result


def test_json():
    file_for_read = open('test/fixtures/test_diff_json_json.txt')
    path_one = 'test/fixtures/examples/file1_rec.json'
    path_two = 'test/fixtures/examples/file2_rec.json'
    result = file_for_read.read()
    test_result = generate_diff(path_one, path_two, format_name='json')
    assert result == test_result
