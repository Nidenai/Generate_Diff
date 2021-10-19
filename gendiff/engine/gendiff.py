from gendiff.engine.parsing import generate_differenses
from gendiff.formats.var import FORMATS
from gendiff.cli import get_data


def generate_diff(file1, file2, format_name='stylish'):
    file1, file2 = parsing(file1, file2)
    return FORMATS[format_name](get_data(file1, file2))


def parsing(file1, file2):
    return generate_differenses(file1, file2)