from gendiff.engine.differ import generate_diff
from test.constants import DIFF_BASE, DIFF_REC, DIFF_PLAIN, DIFF_JSON, FILE_YAML_REC1, FILE_YAML_REC2, FILE_YAML1, FILE_YAML2


def test_base():
    file_for_read = open(DIFF_BASE)
    result = file_for_read.read()
    test_result = generate_diff(FILE_YAML1, FILE_YAML2)
    assert result == test_result


def test_plain():
    file_for_read = open(DIFF_PLAIN)
    result = file_for_read.read()
    test_result = generate_diff(FILE_YAML_REC1, FILE_YAML_REC2, format_name='plain')
    assert result == test_result


def test_json():
    file_for_read = open(DIFF_JSON)
    result = file_for_read.read()
    test_result = generate_diff(FILE_YAML_REC1, FILE_YAML_REC2, format_name='json')
    assert result == test_result
