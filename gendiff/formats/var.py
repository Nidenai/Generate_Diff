from gendiff.formats import stylish
from gendiff.formats import json
from gendiff.formats import plain


FORMATS = {
    "stylish": stylish.render,
    'json': json.render,
    'plain': plain.render
}
