#!/usr/bin/env python
# coding=utf-8

from distutils.core import setup

version = '0.3'

setup(
    name='jefferson',
    version=version,
    description='JFFS2 filesystem extraction tool originally released by Stefan Viehböck. Python3 update by Jaan Klouman',
    author='Stefan Viehböck & Jaan Klouman',
    url='https://github.com/sviehb/jefferson',
    license='MIT',

    requires=['cstruct'],
    packages=['jefferson'],
    package_dir={'jefferson': 'src/jefferson'},
    scripts=['src/scripts/jefferson'],
)