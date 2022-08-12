from setuptools import setup
from typing import List   # this list is a list which will have str elements



# declaring variables for setup functions

PROJECT_NAME='housing-predictor'
VERSION="0.0.1"
AUTHOR="marshel"
DESCRIPTION='this is the first ml project experimenting'
PACKAGES=['housing']
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:  # going to return list which have str values
    ''' 
    Description: this functions is going to return list of requirement mention in requirement.txt file 
    
    return: this function is going to return a list which contain name of libraries mentioned in requirements.txt file  '''

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines()



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
descriptions=DESCRIPTION,
packages=PACKAGES, # housing folder indication  indicating libraries from that folder will get installed 
install_requires=get_requirements_list() #  requirements.txt libraries will be installed and returned in the list 

)


