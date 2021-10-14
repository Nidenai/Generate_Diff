from gendiff.engine import generate_diff



def test_for_json():
    file_for_read = open('test/fixtures/test_file_json.txt')
    path_one = 'test/fixtures/examples/file1.json'
    path_two = 'test/fixtures/examples/file2.json'
    result = file_for_read.read()
    test_result = generate_diff(path_one path_two)
    assert result == test_result

print(test_for_json())


