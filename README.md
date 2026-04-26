# taskio

A simple command-line task tracker written in Python.

## Features:
- Add tasks
- List tasks
- Complete tasks
- Save tasks to JSON
- Load tasks from JSON

## Requirements:
- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) - An extremely fast Python package and project manager, written in Rust.

## Quick start

```bash
git clone https://github.com/aroki1/taskio.git
cd taskio
uv run taskio
```

## Install as a CLI command:
```
git clone https://github.com/aroki1/taskio.git
cd taskio
uv tool install .
```
After installation, run:
`taskio`

**Important**: reinstall after local changes:

`uv tool install . --reinstall`

## Run tests:
```
uv run pytest
```

## Project structure
```
.
├── app
│   ├── errors.py
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── task_repository.py
│   ├── task_service.py
├── pyproject.toml
├── README.md
├── tests
│   ├── __init__.py
│   └── test_task_service.py
```