import os
from pathlib import Path
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

def create_directory(filepath):
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

def create_empty_file(filepath):
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath.name} already exists")

def create_project_structure(list_of_files):
    for filepath in list_of_files:
        filepath = Path(filepath)
        create_directory(filepath)
        create_empty_file(filepath)

# Project configuration
project_name = 'Kidney Disease Classifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# Create project structure
create_project_structure(list_of_files)
