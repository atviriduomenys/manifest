from setuptools import setup, find_packages


def requirements(filename):
    with open(filename) as f:
        return list(f)


setup(
    name="admanifest",
    version="0.1",
    license="AGPL",
    url="https://github.com/atviriduomenys/manifest",
    packages=find_packages(),
    install_requires=requirements('requirements.in'),
    entry_points={
        'console_scripts': [
            'admanifest-check = admanifest.scripts.check:main',
        ],
    }
)
