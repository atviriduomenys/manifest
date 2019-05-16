from setuptools import setup


def read_requirements(filename):
    with open(filename) as f:
        for req in f:
            if '#egg=' in req:
                req = req.partition('#egg=')[2]
            req = req.partition('#')[0].strip()
            if req:
                yield req


setup(
    name='lithuanian-open-data-manifest',
    description='Open Data Manifest.',
    author='Mantas Zimnickas',
    author_email='sirexas@gmail.com',
    version='0.0.1',
    licence='MIT',
    packages=['lodam'],
    install_requires=list(read_requirements('requirements.in')),
)
