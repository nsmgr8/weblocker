#!/usr/bin/env python

# The MIT License (MIT)
# Copyright (c) 2011 M Nasimul Haque

from distutils.core import setup

from weblocker import VERSION


data_files = [
    ('/usr/share/pixmaps/', ('resources/weblocker.png',),),
    ('/usr/share/applications/', ('resources/weblocker.desktop',),),
]

long_description = open('README.rst', 'r').read()

setup(
    name='WebLocker',
    version=VERSION,
    license='MIT License',
    url='https://github.com/nsmgr8/weblocker',
    download_url='https://github.com/nsmgr8/weblocker/zipball/{0}'.format(VERSION),
    author='M Nasimul Haque',
    author_email='nasim.haque@gmail.com',
    description='A simple GUI for adding/removing sites into /etc/hosts file to block websites',
    long_description=long_description,
    packages=['weblocker'],
    scripts=['weblockerapp'],
    data_files=data_files,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: System :: Systems Administration',
    ],
)

