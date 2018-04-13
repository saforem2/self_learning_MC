# -*- coding: utf-8 -*-

# Learn more: https://github.com/saforem2/self_learning_MC

from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import self_learning_MC

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


#  with open('README.rst') as f:
#      readme = f.read()
long_description = read('README.md')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='self_learning_MC',
    version='0.1.0',
    description='Self learning Monte-Carlo algorithm for 2D spin models',
    long_description=long_description,
    author='Sam Foreman',
    author_email='samuel-foreman@uiowa.edu',
    url='https://github.com/saforem2/self_learning_MC',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    include_package_data=True,
    test_suite='tests.test_self_learning_MC',
    extras_require={
        'testing': ['pytest'],
    }
)


python-targets: 3
