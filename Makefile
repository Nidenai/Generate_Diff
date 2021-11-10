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


start:
	export PATH="$HOME/.poetry/bin:$PATH"
	export PATH="$HOME/.local/bin:$PATH"


coverage:
	poetry run coverage run -m pytest -v



