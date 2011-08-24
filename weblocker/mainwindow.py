
# The MIT License (MIT)
# Copyright (c) 2011 M Nasimul Haque

import re

from PySide import QtGui

from .mainwindow_ui import Ui_MainWindow
from .models import HostsFile, Backup

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    host_re = re.compile(r'^((.*?)(://+)){0,1}([^/?#:]*)')

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.hosts_model = HostsFile()
        self.listView.setModel(self.hosts_model)
        self.backup_model = Backup()
        self.backupListView.setModel(self.backup_model)

        self._create_connections()
        self.dirty = False
        self.load_hosts_file()
        self.currentHostsText.setHidden(True)

    def _create_connections(self):
        self.blockButton.clicked.connect(self.add_site)
        self.unblockButton.clicked.connect(self.remove_sites)
        self.saveButton.clicked.connect(self.save_hosts)
        self.backupListView.selectionModel().selectionChanged.connect(self.show_hosts)
        self.restoreButton.clicked.connect(self.restore_hosts)
        self.cleanButton.clicked.connect(self.clean_backups)
        self.refreshButton.clicked.connect(self.refresh)
        self.importButton.clicked.connect(self.import_sites)
        self.hosts_model.hosts_modified.connect(self.load_hosts_file)

    def load_hosts_file(self):
        self.currentHostsText.setPlainText(open(self.hosts_model.HOSTS_FILE, 'r').read())

    def import_sites(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Import File')
        if filename:
            filename = filename[0]
        else:
            return
        with file(filename, 'r') as f:
            for site in f:
                site = site.strip()
                if not site:
                    continue
                site = site.split()[0]
                m = self.host_re.match(site)
                if m:
                    site = m.groups()[3]
                    if site and site not in self.hosts_model.blocked_sites:
                        self.hosts_model.blocked_sites.append(site)
                        self.dirty = True
        self.hosts_model.reset()

    def add_site(self):
        site = self.lineEdit.text().strip()
        m = self.host_re.match(site)
        if m:
            site = m.groups()[3]
        else:
            return

        if site and site not in self.hosts_model.blocked_sites:
            self.hosts_model.blocked_sites.append(site)
            self.hosts_model.reset()
            self.dirty = True
            self.lineEdit.clear()

    def remove_sites(self):
        remove_list = []
        for item in self.listView.selectedIndexes():
            remove_list.append(self.hosts_model.blocked_sites[item.row()])
        for site in remove_list:
            self.hosts_model.blocked_sites.remove(site)
        if remove_list:
            self.dirty = True
            self.hosts_model.reset()

    def save_hosts(self):
        if self.dirty:
            if self.hosts_model.write_hosts():
                self.backup_model.get_backups()
                self.hostsText.clear()
                self.dirty = False
                self.statusbar.showMessage('Changes have been saved. A backup is also created.')
        else:
            self.statusbar.showMessage('No changes have been made, not saving.')

    def show_hosts(self, new, old):
        try:
            f = self.backup_model.backups[new.indexes()[0].row()][0]
            self.hostsText.setPlainText(open(f, 'r').read())
        except IndexError:
            return

    def restore_hosts(self):
        index = self.backupListView.currentIndex()
        if index.row() >= 0:
            if self.backup_model.restore(index.row()):
                self.hosts_model.read_hosts()
                self.hostsText.clear()
                self.dirty = False
                self.load_hosts_file()

    def clean_backups(self):
        answer = QtGui.QMessageBox.critical(self, self.windowTitle(),
                'This will remove all backups from the system. This cannot be undone!',
                QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        if answer == QtGui.QMessageBox.Cancel:
            return
        self.backup_model.clean()
        self.hostsText.clear()

    def refresh(self):
        index = self.tabWidget.currentIndex()
        if index == 0:
            self.hosts_model.read_hosts()
            self.load_hosts_file()
            self.dirty = False
        else:
            self.backup_model.get_backups()

    def closeEvent(self, event):
        if self.dirty:
            answer = QtGui.QMessageBox.warning(self, self.windowTitle(), 'There are unsaved changes available. Are you sure to quit?',
                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if answer == QtGui.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

