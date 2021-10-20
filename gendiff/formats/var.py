from gendiff.formats import json, plain, stylish

FORMATS = {
    "stylish": stylish.render,
    'json': json.render,
    'plain': plain.render
}
