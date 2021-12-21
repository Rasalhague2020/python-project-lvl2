install:
	poetry install

lint:
	poetry run flake8 gendiff

run-gendiff:
	poetry run gendiff 123 456

test:
	poetry run pytest

build:
	rm ./dist/*.whl
	rm ./dist/*.gz
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall hexlet-code	