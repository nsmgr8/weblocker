# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/mainwindow.ui'
#
# Created: Wed Aug 24 20:41:29 2011
#      by: pyside-uic 0.2.11 running on PySide 1.0.5
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.BlockedSites = QtGui.QWidget()
        self.BlockedSites.setObjectName("BlockedSites")
        self.verticalLayout = QtGui.QVBoxLayout(self.BlockedSites)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.BlockedSites)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.BlockedSites)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.blockButton = QtGui.QPushButton(self.BlockedSites)
        self.blockButton.setObjectName("blockButton")
        self.horizontalLayout.addWidget(self.blockButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listView = QtGui.QListView(self.BlockedSites)
        self.listView.setAlternatingRowColors(True)
        self.listView.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.currentHostsText = QtGui.QPlainTextEdit(self.BlockedSites)
        self.currentHostsText.setReadOnly(True)
        self.currentHostsText.setObjectName("currentHostsText")
        self.verticalLayout.addWidget(self.currentHostsText)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.importButton = QtGui.QPushButton(self.BlockedSites)
        self.importButton.setObjectName("importButton")
        self.horizontalLayout_2.addWidget(self.importButton)
        self.hostsButton = QtGui.QPushButton(self.BlockedSites)
        self.hostsButton.setCheckable(True)
        self.hostsButton.setObjectName("hostsButton")
        self.horizontalLayout_2.addWidget(self.hostsButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.unblockButton = QtGui.QPushButton(self.BlockedSites)
        self.unblockButton.setObjectName("unblockButton")
        self.horizontalLayout_2.addWidget(self.unblockButton)
        self.saveButton = QtGui.QPushButton(self.BlockedSites)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.BlockedSites, "")
        self.Backups = QtGui.QWidget()
        self.Backups.setObjectName("Backups")
        self.gridLayout_2 = QtGui.QGridLayout(self.Backups)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.backupListView = QtGui.QListView(self.Backups)
        self.backupListView.setAlternatingRowColors(True)
        self.backupListView.setObjectName("backupListView")
        self.gridLayout_2.addWidget(self.backupListView, 0, 0, 1, 5)
        spacerItem1 = QtGui.QSpacerItem(534, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 2, 1, 1)
        self.restoreButton = QtGui.QPushButton(self.Backups)
        self.restoreButton.setObjectName("restoreButton")
        self.gridLayout_2.addWidget(self.restoreButton, 3, 4, 1, 1)
        self.hostsText = QtGui.QPlainTextEdit(self.Backups)
        self.hostsText.setEnabled(True)
        self.hostsText.setReadOnly(True)
        self.hostsText.setObjectName("hostsText")
        self.gridLayout_2.addWidget(self.hostsText, 1, 0, 1, 5)
        self.cleanButton = QtGui.QPushButton(self.Backups)
        self.cleanButton.setObjectName("cleanButton")
        self.gridLayout_2.addWidget(self.cleanButton, 3, 3, 1, 1)
        self.tabWidget.addTab(self.Backups, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        self.quitButton.setObjectName("quitButton")
        self.horizontalLayout_3.addWidget(self.quitButton)
        self.refreshButton = QtGui.QPushButton(self.centralwidget)
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout_3.addWidget(self.refreshButton)
        spacerItem2 = QtGui.QSpacerItem(118, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.quitButton, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL("returnPressed()"), self.blockButton.click)
        QtCore.QObject.connect(self.hostsButton, QtCore.SIGNAL("toggled(bool)"), self.currentHostsText.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "WebLocker", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Enter website", None, QtGui.QApplication.UnicodeUTF8))
        self.blockButton.setText(QtGui.QApplication.translate("MainWindow", "Add to &Block List", None, QtGui.QApplication.UnicodeUTF8))
        self.importButton.setToolTip(QtGui.QApplication.translate("MainWindow", "You can bulk add sites from a file. The sites must be in separate lines.", None, QtGui.QApplication.UnicodeUTF8))
        self.importButton.setText(QtGui.QApplication.translate("MainWindow", "&Import", None, QtGui.QApplication.UnicodeUTF8))
        self.hostsButton.setText(QtGui.QApplication.translate("MainWindow", "Show &Hosts File", None, QtGui.QApplication.UnicodeUTF8))
        self.unblockButton.setText(QtGui.QApplication.translate("MainWindow", "&Unblock Selected Site(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BlockedSites), QtGui.QApplication.translate("MainWindow", "Blocked Sites", None, QtGui.QApplication.UnicodeUTF8))
        self.restoreButton.setText(QtGui.QApplication.translate("MainWindow", "Re&store", None, QtGui.QApplication.UnicodeUTF8))
        self.cleanButton.setText(QtGui.QApplication.translate("MainWindow", "&Clean Backups", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Backups), QtGui.QApplication.translate("MainWindow", "Backups", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshButton.setText(QtGui.QApplication.translate("MainWindow", "Re&fresh", None, QtGui.QApplication.UnicodeUTF8))
