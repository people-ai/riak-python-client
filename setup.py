#!/usr/bin/env python

import codecs
import sys

from setuptools import setup, find_packages
from version import get_version
from commands import setup_timeseries, build_messages

install_requires = ['six >= 1.8.0', 'basho_erlastic >= 2.1.1']
requires = ['six(>=1.8.0)', 'basho_erlastic(>= 2.1.1)']

install_requires.append('protobuf >=4.21.5, <5.0')
requires.append('protobuf(>=4.21.5, <5.0)')

with codecs.open('README.md', 'r', 'utf-8') as f:
    readme_md = f.read()

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    with codecs.open('README.rst', 'w', 'utf-8') as f:
        f.write(long_description)
except(IOError, ImportError):
    long_description = readme_md

setup(
    name='riak',
    version=get_version(),
    packages=find_packages(),
    requires=requires,
    install_requires=install_requires,
    package_data={'riak': ['erl_src/*']},
    description='Python client for Riak',
    long_description=long_description,
    zip_safe=True,
    include_package_data=True,
    license='Apache 2',
    platforms='Platform Independent',
    author='Basho Technologies',
    author_email='clients@basho.com',
    test_suite='riak.tests.suite',
    url='https://github.com/basho/riak-python-client',
    cmdclass={
        'build_messages': build_messages,
        'setup_timeseries': setup_timeseries
    },
    classifiers=['License :: OSI Approved :: Apache Software License',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3.9',
                 'Topic :: Database']
    )
