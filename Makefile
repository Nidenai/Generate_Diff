install:
	poetry install


lint:
	poetry run flake8 gendiff


build:
	poetry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl


all:
	make install
	make build
	make publish
	make package-install


go:
	poetry run gendiff -f stylish examples/file_one.json examples/file_two.json


gogo:
	poetry run gendiff -f stylish examples/file1_rec.json examples/file2_rec.json


start:
	export PATH="$HOME/.poetry/bin:$PATH"
	export PATH="$HOME/.local/bin:$PATH"


go_yaml:
	poetry run gendiff -f examples/file_one.yaml examples/file_two.yaml


