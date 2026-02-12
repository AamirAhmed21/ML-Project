from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
     mentioned in the requirements.txt file
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.read().splitlines()
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.1',
    author='Aamir Ahmed',
    author_email="aamirahmed2132@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirement.txt"),
)