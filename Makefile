install:
	poetry install

lint:
	poetry run flake8 brain_games

publish:
	poetry publish -r python-project-lvl1 --build