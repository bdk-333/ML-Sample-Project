from setuptools import setup, find_packages
from pathlib import Path
from typing import List



def get_requirements(file_path: str = "requirements.txt") -> List[str]:
    """Read the requirements from a file and return them as a list."""
    with open(file_path, "r") as file:
        requirements = file.readlines()
    return [req.strip() for req in requirements if req.strip() and not req.startswith("#")]




setup(
    name="My Sample ML Project",
    version="0.1.0",
    author="Kirtankumar Parekh",
    author_email="blackdragon.k333@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

