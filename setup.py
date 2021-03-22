from setuptools import setup, find_packages

setup(
    name='testgear',
    version='0.0.1',
    url='https://github.com/PhilippCo/testgear',
    author='Philipp Cochems',
    author_email='philipp.cochems@gmail.com',
    description='Package to control test gear',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'pyvisa', 'pyvisa-py'],
)
