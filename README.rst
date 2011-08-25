
WebLocker
=========

A simple graphical front-end to add/remove blocking sites to the /etc/hosts
file on POSIX system. This software does not come with any warranty. Use at
your own risk. I would not take responsibility for blowing up your system
because of bug in this software.

This just adds/removes a desired site to the /etc/hosts file as following in its
own block::

    127.0.0.1   www.example.com
    and so on...

Install
=======

This software requires PySide >= 1.0.1, a Qt4 binding for python. Following is
the required steps for installing it on Ubuntu::

    $ sudo apt-add-repository ppa:pyside
    $ sudo apt-get update
    $ sudo apt-get install python-pyside python-pip
    $ sudo pip install weblocker

After this you can run it via the commandline::

    $ sudo weblockerapp

There will also be a menu entry at::

    Applications > System > WebLocker

Note that, this software modifies/writes system files. Therefore, it requires to
be run as root user.

License
=======

The MIT License (MIT)

Copyright (c) 2011 M. Nasimul Haque

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Acknowledgement
===============

Icon courtesy by `Webdesigner Depot`_.

.. _Webdesigner Depot : http://www.webdesignerdepot.com/

