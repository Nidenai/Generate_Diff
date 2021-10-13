from gendiff.engine import gendiff



def test_for_yaml():
    file_for_read = open('test/fixtures/test_file_yaml.txt')
    result = file_for_read.read()
    test_result = gendiff.generate_diff('examples/file_one.yaml', 'examples/file_two.yaml')
    assert result == test_result