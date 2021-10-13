from gendiff.engine import gendiff



def test_for_json():
    file_for_read = open('test/fixtures/test_file_json.txt')
    result = file_for_read.read()
    test_result = gendiff.generate_diff('examples/file_one.json', 'examples/file_two.json')
    assert result == test_result
