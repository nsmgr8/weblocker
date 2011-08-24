#!/usr/bin/env python

# The MIT License (MIT)
# Copyright (c) 2011 M Nasimul Haque

from distutils.core import setup

from weblocker import VERSION

try:
    long_description = open('README.rst', 'r').read()
except:
    long_description = ''

setup(
    name='WebLocker',
    version=VERSION,
    url='https://github.com/nsmgr8/weblocker',
    download_url='https://github.com/nsmgr8/weblocker/zipball/{0}'.format(VERSION),
    author='M Nasimul Haque',
    author_email='nasim.haque@gmail.com',
    description='A simple GUI for adding/removing sites into /etc/hosts file to block websites',
    long_description=long_description,
    packages=['weblocker'],
    scripts=['weblockerapp'],
    classifiers=['Development Status :: 3 - Alpha',
                 'Environment :: X11 Applications :: Qt',
                 'Intended Audience :: End Users/Desktop',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: POSIX',
                 'Topic :: System :: Systems Administration',
    ],
)

