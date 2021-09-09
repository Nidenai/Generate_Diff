install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

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

gendiff:
	poetry run gendiff


go:
	poetry run gendiff -f j examples/file_one.json examples/file_one.json


start:
	export PATH="$HOME/.poetry/bin:$PATH"