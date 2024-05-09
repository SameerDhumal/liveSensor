from setuptools import find_packages,   setup
from typing import List

def get_req() -> List[str]:
    return []

setup(
    name='sensor',
    version='0.0.1',
    author='Sameer',
    author_email='samdhumal25@gmail.com',
    packages=find_packages(),
    install_requires=get_req(),
)

