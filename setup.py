#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'PyYAML==5.4',
    'jinja2==2.10.1',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyresume',
    version='0.1.3',
    description="Populate a predefined LaTeX template with contents defined in YAML to build your resume.",
    long_description=readme + '\n\n' + history,
    author="Wayne Warren",
    author_email='wayne.warren.s@gmail.com',
    url='https://github.com/waynr/pyresume',
    packages=find_packages('src'),
    package_dir={'':
                 'src'},
    entry_points={
        'console_scripts': [
            'pyresume=pyresume.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='pyresume',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
