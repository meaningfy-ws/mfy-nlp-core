from setuptools import find_packages, setup

REQUIREMENTS_FILE_NAME = 'requirements/requirements-lock.txt'

install_requirements = []

with open(REQUIREMENTS_FILE_NAME) as file:
    install_requirements = file.read().splitlines()
    #install_requirements = list(map(str.strip,file.read().splitlines()))

setup(
    name='mfy_nlp_core',
    packages=find_packages(include=['mfy_nlp_core','mfy_nlp_core_fakes']),
    version='0.0.1',
    description='A library used by the Meaningfy team to manage dependencies to third party libraries for NLP tasks.',
    author='Meaningfy',
    license='Apache License 2.0',
    install_requires=install_requirements,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)