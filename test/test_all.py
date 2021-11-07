import test_json
import test_yaml


def test_all():
    test_json.test_base()
    test_json.test_plain()
    test_json.test_json()
    test_yaml.test_base()
    test_yaml.test_plain()
    test_yaml.test_json()


test_all()
