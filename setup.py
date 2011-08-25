#!/usr/bin/env python

# The MIT License (MIT)
# Copyright (c) 2011 M Nasimul Haque

import os
import shutil

from distutils.core import setup
from distutils.command.install_data import install_data

from weblocker import VERSION


class post_install(install_data):
    def run(self):
        install_data.run(self)
        for f in data_files:
            # FIXME: very very ugly hack
            file_to_copy = f[0].replace('resources', self.install_dir)
            dest_file = f[1]
            shutil.copy(file_to_copy, dest_file)
            os.remove(file_to_copy)


data_files = [
    ('resources/weblocker.png', '/usr/share/pixmaps/weblocker.png'),
    ('resources/weblocker.desktop', '/usr/share/applications/weblocker.desktop'),
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
    data_files=[f[0] for f in data_files],
    cmdclass=dict(install_data=post_install),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: System :: Systems Administration',
    ],
)

