# Clean Architecture template with Python

This is a template for a Python project that attempts to follow the Clean Architecture principles.

## Pre-requisites

- Python 3.8
- Docker
- Docker Composer
- Pip

## Installation

Install the dependencies using the following command:
```bash
pip install -r requirements.txt
```

Docker dependencies:
```bash
docker-compose up -d
```

### Starting the application

```bash
uvicorn main:app --reload --port 3000
```
or
```bash
python main.py
```

### Updating the requirements file

```bash
pip freeze > requirements.txt
```

## Troubleshooting

### Uninstalling all dependencies

```bash
pip freeze | xargs pip uninstall -y
```
