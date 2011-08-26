
# The MIT License (MIT)
# Copyright (c) 2011 M Nasimul Haque

import time
import shutil
import glob
import re
import os

from PySide import QtCore, QtGui


class HostsFile(QtCore.QAbstractTableModel):
    HOSTS_FILE = '/etc/hosts'
    BLOCK_OPENER = '# WEBLOCKER START'
    BLOCK_CLOSING = '# WEBLOCKER END'

    hosts_modified = QtCore.Signal()

    def __init__(self, parent=None):
        super(HostsFile, self).__init__(parent=parent)
        self.read_hosts()

    @property
    def header(self):
        return ('Blocked sites',)

    def rowCount(self, parent):
        return len(self.blocked_sites)

    def columnCount(self, parent):
        return len(self.header)

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.header[section]
            else:
                return section + 1
        if role == QtCore.Qt.TextAlignmentRole and orientation == QtCore.Qt.Vertical:
            return QtCore.Qt.AlignRight

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.blocked_sites[index.row()]
        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter

    def read_hosts(self):
        block = False
        self.blocked_sites = []
        self.others = []
        with file(self.HOSTS_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line == self.BLOCK_OPENER:
                    block = True
                    continue
                if line == self.BLOCK_CLOSING:
                    block = False
                    continue
                if block:
                    self.blocked_sites.append(line.split()[1])
                else:
                    self.others.append(line)

        self.reset()

    def write_hosts(self):
        backup = '%s.%f' % (self.HOSTS_FILE, time.time())
        try:
            shutil.copyfile(self.HOSTS_FILE, backup)
        except IOError:
            root_required()
            return False

        with file(self.HOSTS_FILE, 'w') as f:
            f.write('\n'.join(self.others))
            f.write('\n')
            if self.blocked_sites:
                f.write(self.BLOCK_OPENER)
                f.write('\n')
                f.write('\n'.join(['\t'.join(['127.0.0.1', site]) for site in self.blocked_sites]))
                f.write('\n')
                f.write(self.BLOCK_CLOSING)
                f.write('\n')
        self.hosts_modified.emit()
        return True


class Backup(QtCore.QAbstractTableModel):

    r = re.compile('^/etc/hosts\.([0-9\.]+)$')

    def __init__(self, parent=None):
        super(Backup, self).__init__(parent=parent)
        self.get_backups()

    @property
    def header(self):
        return ('Hosts Backups',)

    def rowCount(self, parent):
        return len(self.backups)

    def columnCount(self, parent):
        return len(self.header)

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.header[section]
            else:
                return section + 1

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.backups[index.row()][1]

    def get_backups(self):
        self.backups = []
        files = sorted(glob.glob('/etc/hosts.*'), reverse=True)
        for f in files:
            m = self.r.match(f)
            if m:
                self.backups.append((f, time.ctime(float(m.groups()[0]))))
        self.reset()

    def restore(self, index):
        try:
            backup = self.backups[index][0]
            shutil.copyfile(backup, HostsFile.HOSTS_FILE)
            os.remove(backup)
            self.get_backups()
            return True
        except IndexError:
            pass
        except IOError:
            root_required()
        return False

    def clean(self):
        for f, _ in self.backups:
            os.remove(f)
        self.get_backups()

def root_required():
    window = QtGui.qApp.activeWindow()
    QtGui.QMessageBox.critical(window, window.windowTitle(), 'This program requires root access. Try running it with sudo.')

