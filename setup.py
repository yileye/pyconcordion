#!/usr/bin/env python
from distutils.core import setup
import concordion

setup(name='PyConcordion',
      version=concordion.VERSION,
      description='Concordion python port',
      author='John Jiang',
      author_email='johnjiang101@gmail.com',
      url='https://github.com/johnjiang',
      packages=['concordion', 'concordion.impl'],
      package_data={'concordion': ['*.ini', 'lib/*.jar']},
      scripts=['scripts/concordion_runner', ],
      data_file=[('bin/', ['scripts/concordion_runner', ])]
)
