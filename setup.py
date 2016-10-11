#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from setuptools import setup

requirements = map(str.strip, open("requirements.txt").readlines())

setup(name='oandapy',
      version='0.1',
      description="Library wrapper for the OANDA REST-v20 API",
      author='Gustavo Ferreira',
      author_email='gustavojcoferreira@gmail.com',
      keywords='OANDA FOREX wrapper REST-v20 API',
      license='MIT',
      url='https://github.com/gustavooferreira/oandapy',
      packages=['oandapy', 'tests'],
      test_suite="tests",
      install_requires=requirements,
      classifiers=[
            'Programming Language :: Python',
            'License :: OSI Approved :: MIT License',
            'Intended Audience :: Developers',
            'Intended Audience :: Financial and Insurance Industry'
            'Operating System :: OS Independent',
            'Development Status :: 2 - Pre-Alpha',
            'Topic :: Software Development :: Libraries :: Python Modules'
      ]
      )
