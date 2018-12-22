# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='extendXarray',
    version='0.1.0',
    description='Provides higher level functionality to the Python xarray project by integrating methods from GDAL and OGR.',
    long_description=readme,
    author='Jack McNelis',
    author_email='jjmcnelis@outlook.com',
    url='https://github.com/jjmcnelis/extendXarray',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
