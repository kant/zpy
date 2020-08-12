#!/usr/bin/env python
from distutils.core import setup
from setuptools import find_packages
import versioneer

def get_requirements_from_file(filepath):
    requires = []
    with open(filepath, 'r') as f:
        requires.append(f.readline())
    return requires


setup(
      name='zpy-zumo',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Zumo Labs Utility Bundle',
      author='Zumo Labs',
      author_email='infra@zumolabs.ai',
      packages=find_packages(),
      install_requires=get_requirements_from_file('requirements.txt'),
)