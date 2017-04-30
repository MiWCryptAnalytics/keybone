#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
import os
from setuptools import setup, find_packages

class VersionFinder(ast.NodeVisitor):
    VARIABLE_NAME = 'version'

    def __init__(self):
        self.version = None

    def visit_Assign(self, node):
        try:
            if node.targets[0].id == self.VARIABLE_NAME:
                self.version = node.value.s
        except:
            pass


def read_version():
    finder = VersionFinder()
    finder.visit(ast.parse(local_file('keybone', 'version.py')))
    return finder.version


dependencies = [x.split('==')[0] for x in open('requirements.txt', 'r')]

setup(
    name='keybone',
    version=read_version(),
    description="\n".join([
        'Create/Manage/List GPG Keys and Encrypt/Decrypt things with them'
    ]),
    entry_points={
        'console_scripts': [
            'keybone = keybone.console.main:entrypoint',
            'kb = keybone.console.main:entrypoint',
        ],
    },
    author='Gabriel Falcao',
    author_email='gabriel@nacaolivre.org',
    url='https://github.com/gabrielfalcao/keybone',
    packages=find_packages(exclude=['*tests*']),
    install_requires=dependencies,
    include_package_data=True,
    package_data={
        'keybone': 'COPYING *.rst *.txt docs/source/* docs/*'.split(),
    },
    zip_safe=False,
)
