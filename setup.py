from setuptools import find_packages, setup

REQUIREMENTS_FILE_NAME = 'requirements/requirements-lock.txt'

SPACY_MODEL_NAME = 'en-core-web-md'
SPACY_MODEL_LINK = 'https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.2.0/en_core_web_md-3.2.0-py3-none-any.whl'


install_requirements = []

with open(REQUIREMENTS_FILE_NAME) as file:
    install_requirements = list(map(str.strip,file.read().splitlines()))

setup(
    name='mfy_nlp_core',
    packages=find_packages(include=['mfy_nlp_core','mfy_nlp_core_fakes']),
    version='0.0.1',
    description='A library used by the Meaningfy team to manage dependencies to third party libraries for NLP tasks.',
    author='Meaningfy',
    license='Apache License 2.0',
    install_requires=install_requirements+[SPACY_MODEL_NAME],
    dependency_links = [SPACY_MODEL_LINK],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)