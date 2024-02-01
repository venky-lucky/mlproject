from setuptools import find_packages,setup
from typing import List

 
def get_requiremnts(filepath:str)->List[str]:
    '''
    this function will return the requirenment packages
    '''
    requiremnts = []
    with open(filepath) as file_obj:
        requiremnts = file_obj.readlines()
        requiremnts = [req.replace("\n","") for req in requiremnts]
    if "-e." in requiremnts:
        requiremnts.remove("-e.")

setup(
   name="mlproject",
   version="0.0.1",
   author="venkatesh",
   author_email="venkateshmoturi79@gmail.com",
   packages=find_packages(),
   install_requires = get_requiremnts('requirements.txt') 
)