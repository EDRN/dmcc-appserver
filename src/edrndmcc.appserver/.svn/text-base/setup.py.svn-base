# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from setuptools import setup, find_packages
import os

version = '1.0.1'

setup(
    name='edrndmcc.appserver',
    version=version,
    description="EDRN DMCC Application Server policy",
    long_description=open('README.txt').read() + '\n' + open(os.path.join('docs', 'HISTORY.txt')).read(),
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='web policy zope plone jpl nasa caltech edrn cancer detection appserver application server',
    author='Sean Kelly',
    author_email='sean.kelly@jpl.nasa.gov',
    url='http://cancer.jpl.nasa.gov/products/edrndmcc-appserver',
    download_url='http://oodt.jpl.nasa.gov/dist/edrndmcc-appserver',
    license='Proprietary',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['edrndmcc'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'edrn.theme',
        'edrn.rdf',
    ],
    entry_points={},
)
