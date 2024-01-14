from setuptools import setup, find_packages

HYPEN_E_DOT = '-e .'

def get_requirements(file_path='requirements.txt'):
    """
    Reads a file and returns a list of requirements.

    :param file_path: The path to the requirements file. Default is 'requirements.txt'.
    :return: A list of requirements.
    """
    with open(file_path, 'rt') as f:
        requirements = [line.strip() for line in f]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='census_salary_prediction',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements(file_path='requirements.txt'),
    author='Rahul Yadav and Suraj Yadav',
    author_email='rahul.yadav.264868@gmail.com',
    description='Adult Census Salary Price Prediction',
)
