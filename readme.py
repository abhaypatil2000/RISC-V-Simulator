# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readme.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_README(object):
    def setupUi(self, README):
        README.setObjectName("README")
        README.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(README)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        README.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(README)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        README.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(README)
        self.statusbar.setObjectName("statusbar")
        README.setStatusBar(self.statusbar)

        self.retranslateUi(README)
        QtCore.QMetaObject.connectSlotsByName(README)
        with open("final_readme.txt") as f:
            file_text=f.read()
            self.textBrowser.setText(file_text)

    def retranslateUi(self, README):
        _translate = QtCore.QCoreApplication.translate
        README.setWindowTitle(_translate("README", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    README = QtWidgets.QMainWindow()
    ui = Ui_README()
    ui.setupUi(README)
    README.show()
    sys.exit(app.exec_())

