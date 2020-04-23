#!/usr/bin/env python
"""Assemblyline Client Library PiP Installer"""

import os
from setuptools import setup, find_packages

# This lets us avoid importing the client before it in installed
package_version = "4.0.0.dev0"
for variable_name in ['BITBUCKET_TAG']:
    package_version = os.environ.get(variable_name, package_version)
    package_version = package_version.lstrip('v')

# read the contents of the README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='assemblyline-client',
    version=package_version,
    description='Assemblyline v4 client library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/CybercentreCanada/assemblyline-client',
    author='CSE-CST Assemblyline development team',
    author_email='assemblyline@cyber.gc.ca',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    entry_points={
        'console_scripts': [
            'al-submit=assemblyline_client.submit:main',
        ],
    },
    install_requires=[
        'pycryptodome',
        'requests',
        'requests[security]',
        'python-baseconv',
        'python-socketio[client]',
        'socketio-client==0.5.7.4'
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
            'cart',
            'assemblyline',
            'passlib',
            'mock',
            'pytest_mock'
        ]
    },
    keywords='development assemblyline client gc canada cse-cst cse cst',
    packages=find_packages(exclude=['test/*'])
)
