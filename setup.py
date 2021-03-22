from setuptools import setup, find_packages

setup(
    name='testpkg',
    version='1.0.0',
    url='https://github.com/PhilippCo/testgear',
    author='Philipp Cochems',
    author_email='philipp.cochems@gmail.com',
    description='Package to control test gear',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'pyvisa', 'pyvisa-py'],
)
