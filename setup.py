from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return [req.strip() for req in requirements]
    

setup(
    name='DiamondPriceprediction',
    version='0.0.1',
    author='Hitesh',
    author_email='ankodiahitesh@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
