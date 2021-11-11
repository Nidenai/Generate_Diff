from gendiff.engine.differ import generate_diff
from test.constants import DIFF_BASE, DIFF_PLAIN, DIFF_JSON, FILE_JSON1, FILE_JSON2, FILE_JSON_REC1, FILE_JSON_REC2, DIFF_REC


def test_base():
    file_for_read = open(DIFF_BASE)
    result = file_for_read.read()
    test_result = generate_diff(FILE_JSON1, FILE_JSON2)
    assert result == test_result


def test_plain():
    file_for_read = open(DIFF_PLAIN)
    result = file_for_read.read()
    test_result = generate_diff(FILE_JSON_REC1, FILE_JSON_REC2, format_name='plain')
    assert result == test_result


def test_json():
    file_for_read = open(DIFF_JSON)
    result = file_for_read.read()
    test_result = generate_diff(FILE_JSON_REC1, FILE_JSON_REC2, format_name='json')
    assert result == test_result
