
# The MIT License (MIT)
# Copyright (c) 2011 M Nasimul Haque

VERSION = '0.3'

def main():
    import sys
    from PySide import QtGui
    from mainwindow import MainWindow

    app = QtGui.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    return app.exec_()

