## Getting Started
### 1. Setting up the environment
To get started on the assigment, you will need the following installed on your PC:
- [Python 3.10](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer): package manager for Python to ensure consistency in package versions

NOTE: on some Windows systems using Poetry can be tricky, in that case just directly install the Python packages in the `tool.poetry.dependencies` section of the `pyproject.toml` file (skipping `pyhton`).

Then we want to create and activate a new virtual environment (commands are for Unix systems, change for Windows accordingly):
```shell
python3.10 -m venv .venv3.10
source ./.venv3.10/bin/activate
poetry install --sync
```

### 2. Run the program
```shell
cd to directory path
python main.py
```
