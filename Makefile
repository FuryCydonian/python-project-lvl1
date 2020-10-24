install:
	poetry install

lint:
	poetry run flake8 brain_games

publish:
	poetry publish -r python-project-lvl1 --build

poetry config:
	poetry config repositories.brain_games https://test.pypi.org/legacy/