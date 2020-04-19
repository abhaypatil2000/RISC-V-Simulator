# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fourth.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from main import *
import main3
from readme import Ui_README
total_lines =0
TepMem=[]
class Ui_MainWindow(object):
    def readme_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui=Ui_README()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1500, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabBar = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabBar.setFont(font)
        self.tabBar.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabBar.setElideMode(QtCore.Qt.ElideLeft)
        self.tabBar.setObjectName("tabBar")
        self.Editor = QtWidgets.QWidget()
        self.Editor.setObjectName("Editor")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Editor)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Edit = QtWidgets.QTextEdit(self.Editor)
        font = QtGui.QFont()
        font.setFamily("Ariel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Edit.setFont(font)
        self.Edit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Edit.setMouseTracking(False)
        self.Edit.setObjectName("Edit")
        self.gridLayout_2.addWidget(self.Edit, 1, 0, 1, 1)
        self.tabBar.addTab(self.Editor, "")
        self.Simulator = QtWidgets.QWidget()
        self.Simulator.setObjectName("Simulator")
        self.Simulator.setEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(self.Simulator)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line = QtWidgets.QFrame(self.Simulator)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(self.Simulator)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.output = QtWidgets.QTextEdit(self.Simulator)
        font = QtGui.QFont()
        font.setFamily("Ariel")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.output.setTextColor(QtGui.QColor(255,255,255))
        self.output.setFont(font)
        self.output.setObjectName("output")
        self.verticalLayout_2.addWidget(self.output)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.Simulator)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.machine_code = QtWidgets.QTextEdit(self.Simulator)
        self.machine_code.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(50)
        self.machine_code.setFont(font)
        self.machine_code.setReadOnly(False)
        self.machine_code.setObjectName("machine_code")
        self.verticalLayout.addWidget(self.machine_code)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Run = QtWidgets.QPushButton(self.Simulator)
        self.Run.setObjectName("Run")
        self.horizontalLayout.addWidget(self.Run)
        self.Step = QtWidgets.QPushButton(self.Simulator)
        self.Step.setObjectName("Step")
        self.horizontalLayout.addWidget(self.Step)
        self.Prev = QtWidgets.QPushButton(self.Simulator)
        self.Prev.setObjectName("Prev")
        self.horizontalLayout.addWidget(self.Prev)
        self.Reset = QtWidgets.QPushButton(self.Simulator)
        self.Reset.setObjectName("Reset")
        self.horizontalLayout.addWidget(self.Reset)
        self.Clear = QtWidgets.QPushButton(self.Simulator)
        self.Clear.setObjectName("Clear")
        self.horizontalLayout.addWidget(self.Clear)
        self.Breakpoint = QtWidgets.QPushButton(self.Simulator)
        self.Breakpoint.setObjectName("Breakpoint")
        self.horizontalLayout.addWidget(self.Breakpoint)
        self.breakline = QtWidgets.QLineEdit(self.Simulator)
        self.breakline.setObjectName("breakline")
        self.horizontalLayout.addWidget(self.breakline)
        
       
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabBar2 = QtWidgets.QTabWidget(self.Simulator)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.tabBar2.setFont(font)
        self.tabBar2.setObjectName("tabBar2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.t0 = QtWidgets.QTextBrowser(self.tab)
        self.t0.setGeometry(QtCore.QRect(90, 10, 131, 31))
        self.t0.setObjectName("t0")
        self.t1 = QtWidgets.QTextBrowser(self.tab)
        self.t1.setGeometry(QtCore.QRect(90, 40, 131, 31))
        self.t1.setObjectName("t1")
        self.t2 = QtWidgets.QTextBrowser(self.tab)
        self.t2.setGeometry(QtCore.QRect(90, 70, 131, 31))
        self.t2.setObjectName("t2")
        self.t3 = QtWidgets.QTextBrowser(self.tab)
        self.t3.setGeometry(QtCore.QRect(90, 100, 131, 31))
        self.t3.setObjectName("t3")
        self.t4 = QtWidgets.QTextBrowser(self.tab)
        self.t4.setGeometry(QtCore.QRect(90, 130, 131, 31))
        self.t4.setObjectName("t4")
        self.t5 = QtWidgets.QTextBrowser(self.tab)
        self.t5.setGeometry(QtCore.QRect(90, 160, 131, 31))
        self.t5.setObjectName("t5")
        self.t6 = QtWidgets.QTextBrowser(self.tab)
        self.t6.setGeometry(QtCore.QRect(90, 190, 131, 31))
        self.t6.setObjectName("t6")
        self.t7 = QtWidgets.QTextBrowser(self.tab)
        self.t7.setGeometry(QtCore.QRect(90, 220, 131, 31))
        self.t7.setObjectName("t7")
        self.t8 = QtWidgets.QTextBrowser(self.tab)
        self.t8.setGeometry(QtCore.QRect(90, 250, 131, 31))
        self.t8.setObjectName("t8")
        self.t9 = QtWidgets.QTextBrowser(self.tab)
        self.t9.setGeometry(QtCore.QRect(90, 280, 131, 31))
        self.t9.setObjectName("t9")
        self.t10 = QtWidgets.QTextBrowser(self.tab)
        self.t10.setGeometry(QtCore.QRect(90, 310, 131, 41))
        self.t10.setObjectName("t10")
        self.t11 = QtWidgets.QTextBrowser(self.tab)
        self.t11.setGeometry(QtCore.QRect(90, 350, 131, 31))
        self.t11.setObjectName("t11")
        self.t12 = QtWidgets.QTextBrowser(self.tab)
        self.t12.setGeometry(QtCore.QRect(90, 380, 131, 31))
        self.t12.setObjectName("t12")
        self.t13 = QtWidgets.QTextBrowser(self.tab)
        self.t13.setGeometry(QtCore.QRect(90, 410, 131, 31))
        self.t13.setObjectName("t13")
        self.x17 = QtWidgets.QLabel(self.tab)
        self.x17.setGeometry(QtCore.QRect(220, 102, 69, 24))
        self.x17.setAlignment(QtCore.Qt.AlignCenter)
        self.x17.setObjectName("x17")
        self.x16 = QtWidgets.QLabel(self.tab)
        self.x16.setGeometry(QtCore.QRect(220, 72, 69, 23))
        self.x16.setAlignment(QtCore.Qt.AlignCenter)
        self.x16.setObjectName("x16")
        self.x22 = QtWidgets.QLabel(self.tab)
        self.x22.setGeometry(QtCore.QRect(220, 256, 69, 24))
        self.x22.setAlignment(QtCore.Qt.AlignCenter)
        self.x22.setObjectName("x22")
        self.x19 = QtWidgets.QLabel(self.tab)
        self.x19.setGeometry(QtCore.QRect(220, 164, 69, 24))
        self.x19.setAlignment(QtCore.Qt.AlignCenter)
        self.x19.setObjectName("x19")
        self.x20 = QtWidgets.QLabel(self.tab)
        self.x20.setGeometry(QtCore.QRect(220, 190, 69, 23))
        self.x20.setAlignment(QtCore.Qt.AlignCenter)
        self.x20.setObjectName("x20")
        self.x15 = QtWidgets.QLabel(self.tab)
        self.x15.setGeometry(QtCore.QRect(220, 40, 69, 24))
        self.x15.setAlignment(QtCore.Qt.AlignCenter)
        self.x15.setObjectName("x15")
        self.x21 = QtWidgets.QLabel(self.tab)
        self.x21.setGeometry(QtCore.QRect(220, 225, 69, 24))
        self.x21.setAlignment(QtCore.Qt.AlignCenter)
        self.x21.setObjectName("x21")
        self.x18 = QtWidgets.QLabel(self.tab)
        self.x18.setGeometry(QtCore.QRect(220, 133, 69, 24))
        self.x18.setAlignment(QtCore.Qt.AlignCenter)
        self.x18.setObjectName("x18")
        self.x14 = QtWidgets.QLabel(self.tab)
        self.x14.setGeometry(QtCore.QRect(220, 10, 69, 24))
        self.x14.setAlignment(QtCore.Qt.AlignCenter)
        self.x14.setObjectName("x14")
        self.t20 = QtWidgets.QTextBrowser(self.tab)
        self.t20.setGeometry(QtCore.QRect(280, 190, 131, 31))
        self.t20.setObjectName("t20")
        self.t14 = QtWidgets.QTextBrowser(self.tab)
        self.t14.setGeometry(QtCore.QRect(280, 11, 131, 31))
        self.t14.setObjectName("t14")
        self.t15 = QtWidgets.QTextBrowser(self.tab)
        self.t15.setGeometry(QtCore.QRect(280, 40, 131, 31))
        self.t15.setObjectName("t15")
        self.t17 = QtWidgets.QTextBrowser(self.tab)
        self.t17.setGeometry(QtCore.QRect(280, 100, 131, 31))
        self.t17.setObjectName("t17")
        self.t16 = QtWidgets.QTextBrowser(self.tab)
        self.t16.setGeometry(QtCore.QRect(280, 70, 131, 31))
        self.t16.setObjectName("t16")
        self.t18 = QtWidgets.QTextBrowser(self.tab)
        self.t18.setGeometry(QtCore.QRect(280, 130, 131, 31))
        self.t18.setObjectName("t18")
        self.t19 = QtWidgets.QTextBrowser(self.tab)
        self.t19.setGeometry(QtCore.QRect(280, 160, 131, 31))
        self.t19.setObjectName("t19")
        self.t22 = QtWidgets.QTextBrowser(self.tab)
        self.t22.setGeometry(QtCore.QRect(280, 250, 131, 41))
        self.t22.setObjectName("t22")
        self.t21 = QtWidgets.QTextBrowser(self.tab)
        self.t21.setGeometry(QtCore.QRect(280, 220, 131, 31))
        self.t21.setObjectName("t21")
        self.x30 = QtWidgets.QLabel(self.tab)
        self.x30.setGeometry(QtCore.QRect(10, 450, 69, 23))
        self.x30.setAlignment(QtCore.Qt.AlignCenter)
        self.x30.setObjectName("x30")
        self.x25 = QtWidgets.QLabel(self.tab)
        self.x25.setGeometry(QtCore.QRect(220, 351, 69, 23))
        self.x25.setAlignment(QtCore.Qt.AlignCenter)
        self.x25.setObjectName("x25")
        self.x28 = QtWidgets.QLabel(self.tab)
        self.x28.setGeometry(QtCore.QRect(220, 443, 69, 24))
        self.x28.setAlignment(QtCore.Qt.AlignCenter)
        self.x28.setObjectName("x28")
        self.x23 = QtWidgets.QLabel(self.tab)
        self.x23.setGeometry(QtCore.QRect(220, 289, 69, 24))
        self.x23.setAlignment(QtCore.Qt.AlignCenter)
        self.x23.setObjectName("x23")
        self.x29 = QtWidgets.QLabel(self.tab)
        self.x29.setGeometry(QtCore.QRect(220, 474, 69, 24))
        self.x29.setAlignment(QtCore.Qt.AlignCenter)
        self.x29.setObjectName("x29")
        self.x27 = QtWidgets.QLabel(self.tab)
        self.x27.setGeometry(QtCore.QRect(220, 412, 69, 24))
        self.x27.setAlignment(QtCore.Qt.AlignCenter)
        self.x27.setObjectName("x27")
        self.x31 = QtWidgets.QLabel(self.tab)
        self.x31.setGeometry(QtCore.QRect(10, 480, 69, 24))
        self.x31.setAlignment(QtCore.Qt.AlignCenter)
        self.x31.setObjectName("x31")
        self.x26 = QtWidgets.QLabel(self.tab)
        self.x26.setGeometry(QtCore.QRect(220, 381, 69, 24))
        self.x26.setAlignment(QtCore.Qt.AlignCenter)
        self.x26.setObjectName("x26")
        self.x24 = QtWidgets.QLabel(self.tab)
        self.x24.setGeometry(QtCore.QRect(220, 320, 69, 24))
        self.x24.setAlignment(QtCore.Qt.AlignCenter)
        self.x24.setObjectName("x24")
        self.t23 = QtWidgets.QTextBrowser(self.tab)
        self.t23.setGeometry(QtCore.QRect(280, 290, 131, 31))
        self.t23.setObjectName("t23")
        self.t25 = QtWidgets.QTextBrowser(self.tab)
        self.t25.setGeometry(QtCore.QRect(280, 350, 131, 31))
        self.t25.setObjectName("t25")
        self.t31 = QtWidgets.QTextBrowser(self.tab)
        self.t31.setGeometry(QtCore.QRect(90, 470, 131, 31))
        self.t31.setObjectName("t31")
        self.t30 = QtWidgets.QTextBrowser(self.tab)
        self.t30.setGeometry(QtCore.QRect(90, 440, 131, 31))
        self.t30.setObjectName("t30")
        self.t24 = QtWidgets.QTextBrowser(self.tab)
        self.t24.setGeometry(QtCore.QRect(280, 320, 131, 31))
        self.t24.setObjectName("t24")
        self.t26 = QtWidgets.QTextBrowser(self.tab)
        self.t26.setGeometry(QtCore.QRect(280, 380, 131, 31))
        self.t26.setObjectName("t26")
        self.t27 = QtWidgets.QTextBrowser(self.tab)
        self.t27.setGeometry(QtCore.QRect(280, 410, 131, 31))
        self.t27.setObjectName("t27")
        self.t29 = QtWidgets.QTextBrowser(self.tab)
        self.t29.setGeometry(QtCore.QRect(280, 470, 131, 31))
        self.t29.setObjectName("t29")
        self.t28 = QtWidgets.QTextBrowser(self.tab)
        self.t28.setGeometry(QtCore.QRect(280, 440, 131, 31))
        self.t28.setObjectName("t28")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(210, 510, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 71, 431))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.x0 = QtWidgets.QLabel(self.layoutWidget)
        self.x0.setAlignment(QtCore.Qt.AlignCenter)
        self.x0.setObjectName("x0")
        self.verticalLayout_5.addWidget(self.x0)
        self.x1 = QtWidgets.QLabel(self.layoutWidget)
        self.x1.setAlignment(QtCore.Qt.AlignCenter)
        self.x1.setObjectName("x1")
        self.verticalLayout_5.addWidget(self.x1)
        self.x2 = QtWidgets.QLabel(self.layoutWidget)
        self.x2.setAlignment(QtCore.Qt.AlignCenter)
        self.x2.setObjectName("x2")
        self.verticalLayout_5.addWidget(self.x2)
        self.x3 = QtWidgets.QLabel(self.layoutWidget)
        self.x3.setAlignment(QtCore.Qt.AlignCenter)
        self.x3.setObjectName("x3")
        self.verticalLayout_5.addWidget(self.x3)
        self.x4 = QtWidgets.QLabel(self.layoutWidget)
        self.x4.setAlignment(QtCore.Qt.AlignCenter)
        self.x4.setObjectName("x4")
        self.verticalLayout_5.addWidget(self.x4)
        self.x5 = QtWidgets.QLabel(self.layoutWidget)
        self.x5.setAlignment(QtCore.Qt.AlignCenter)
        self.x5.setObjectName("x5")
        self.verticalLayout_5.addWidget(self.x5)
        self.x6 = QtWidgets.QLabel(self.layoutWidget)
        self.x6.setAlignment(QtCore.Qt.AlignCenter)
        self.x6.setObjectName("x6")
        self.verticalLayout_5.addWidget(self.x6)
        self.x7 = QtWidgets.QLabel(self.layoutWidget)
        self.x7.setAlignment(QtCore.Qt.AlignCenter)
        self.x7.setObjectName("x7")
        self.verticalLayout_5.addWidget(self.x7)
        self.x8 = QtWidgets.QLabel(self.layoutWidget)
        self.x8.setAlignment(QtCore.Qt.AlignCenter)
        self.x8.setObjectName("x8")
        self.verticalLayout_5.addWidget(self.x8)
        self.x9 = QtWidgets.QLabel(self.layoutWidget)
        self.x9.setAlignment(QtCore.Qt.AlignCenter)
        self.x9.setObjectName("x9")
        self.verticalLayout_5.addWidget(self.x9)
        self.x10 = QtWidgets.QLabel(self.layoutWidget)
        self.x10.setAlignment(QtCore.Qt.AlignCenter)
        self.x10.setObjectName("x10")
        self.verticalLayout_5.addWidget(self.x10)
        self.x11 = QtWidgets.QLabel(self.layoutWidget)
        self.x11.setAlignment(QtCore.Qt.AlignCenter)
        self.x11.setObjectName("x11")
        self.verticalLayout_5.addWidget(self.x11)
        self.x12 = QtWidgets.QLabel(self.layoutWidget)
        self.x12.setAlignment(QtCore.Qt.AlignCenter)
        self.x12.setObjectName("x12")
        self.verticalLayout_5.addWidget(self.x12)
        self.x13 = QtWidgets.QLabel(self.layoutWidget)
        self.x13.setAlignment(QtCore.Qt.AlignCenter)
        self.x13.setObjectName("x13")
        self.verticalLayout_5.addWidget(self.x13)
        self.tabBar2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.memory = QtWidgets.QTextBrowser(self.tab_2)
        self.memory.setGeometry(QtCore.QRect(160, 20, 311, 491))
        self.memory.setObjectName("memory")
        self.tabBar2.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabBar2, 0, 2, 3, 1)
        self.line1 = QtWidgets.QFrame(self.Simulator)
        self.line1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.gridLayout.addWidget(self.line1, 0, 1, 3, 1)
        self.tabBar.addTab(self.Simulator, "")
        self.gridLayout_3.addWidget(self.tabBar, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1244, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPreferences = QtWidgets.QMenu(self.menubar)
        self.menuPreferences.setObjectName("menuPreferences")
        self.menuData_Forwarding = QtWidgets.QMenu(self.menuPreferences)
        self.menuData_Forwarding.setObjectName("menuData_Forwarding")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Open = QtWidgets.QAction(MainWindow)
        self.Open.setObjectName("Open")
        self.Save = QtWidgets.QAction(MainWindow)
        self.Save.setObjectName("Save")
        self.Exit = QtWidgets.QAction(MainWindow)
        self.Exit.setObjectName("Exit")
        self.generate = QtWidgets.QAction(MainWindow)
        self.generate.setEnabled(True)
        self.generate.setObjectName("generate")
        self.Clear_Output = QtWidgets.QAction(MainWindow)
        self.Clear_Output.setObjectName("Clear_Output")
        self.README = QtWidgets.QAction(MainWindow)
        self.README.setObjectName("README")
        self.Enable_P = QtWidgets.QAction(MainWindow)
        self.Enable_P.setCheckable(True)
        self.Enable_P.setChecked(False)
        self.Enable_P.setObjectName("Enable_P")
        self.EnabledD = QtWidgets.QAction(MainWindow)
        self.EnabledD.setCheckable(True)
        self.EnabledD.setObjectName("EnabledD")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.Open)
        self.menuFile.addAction(self.Save)
        self.menuFile.addAction(self.Exit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.generate)
        self.menuData_Forwarding.addAction(self.EnabledD)
        self.menuPreferences.addAction(self.Clear_Output)
        self.menuPreferences.addAction(self.Enable_P)
        self.menuPreferences.addAction(self.menuData_Forwarding.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.Open)
        self.menuFile.addAction(self.Save)
        self.menuFile.addAction(self.Exit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.generate)
        self.menuPreferences.addAction(self.Clear_Output)
        self.menuHelp.addAction(self.README)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
    

        self.retranslateUi(MainWindow)
        self.tabBar.setCurrentIndex(0)
        self.tabBar2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Edit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Georgia\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Sans Serif\';\">Enter your Assemble code here</span></p></body></html>"))
        self.tabBar.setTabText(self.tabBar.indexOf(self.Editor), _translate("MainWindow", "Editor"))
        self.label_2.setText(_translate("MainWindow", "Console Output "))
        self.output.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:8pt; font-weight:400; font-style:italic;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:12pt; font-weight:600; font-style:normal;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Machine Code"))
        self.machine_code.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Georgia\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Sans Serif\'; font-size:12pt;\">machine code </span></p></body></html>"))
        self.Run.setText(_translate("MainWindow", "Run"))
        self.Step.setText(_translate("MainWindow", "Step"))
        self.Prev.setText(_translate("MainWindow", "Prev"))
        self.Breakpoint.setText(_translate("MainWindow", "Breakpoint"))
        self.Reset.setText(_translate("MainWindow", "Reset"))
        self.Clear.setText(_translate("MainWindow", "Clear "))
        self.t0.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.x17.setText(_translate("MainWindow", "X17-"))
        self.x16.setText(_translate("MainWindow", "X16-"))
        self.x22.setText(_translate("MainWindow", "X22-"))
        self.x19.setText(_translate("MainWindow", "X19-"))
        self.x20.setText(_translate("MainWindow", "X20-"))
        self.x15.setText(_translate("MainWindow", "X15-"))
        self.x21.setText(_translate("MainWindow", "X21-"))
        self.x18.setText(_translate("MainWindow", "X18-"))
        self.x14.setText(_translate("MainWindow", "X14-"))
        self.t20.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t14.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t15.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t17.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t16.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t18.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t19.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t22.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t21.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.x30.setText(_translate("MainWindow", "X30-"))
        self.x25.setText(_translate("MainWindow", "X25-"))
        self.x28.setText(_translate("MainWindow", "X28-"))
        self.x23.setText(_translate("MainWindow", "X23-"))
        self.x29.setText(_translate("MainWindow", "X29-"))
        self.x27.setText(_translate("MainWindow", "X27-"))
        self.x31.setText(_translate("MainWindow", "X31-"))
        self.x26.setText(_translate("MainWindow", "X26-"))
        self.x24.setText(_translate("MainWindow", "X24-"))
        self.t23.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t25.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t31.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t30.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t26.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t27.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t29.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.t28.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Sans Serif\'; font-size:10pt; font-style:italic;\"><br /></p></body></html>"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Hex"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Decimal"))
        self.x0.setText(_translate("MainWindow", "X0-"))
        self.x1.setText(_translate("MainWindow", "X1-"))
        self.x2.setText(_translate("MainWindow", "X2-"))
        self.x3.setText(_translate("MainWindow", "X3-"))
        self.x4.setText(_translate("MainWindow", "X4-"))
        self.x5.setText(_translate("MainWindow", "X5-"))
        self.x6.setText(_translate("MainWindow", "X6-"))
        self.x7.setText(_translate("MainWindow", "X7-"))
        self.x8.setText(_translate("MainWindow", "X8-"))
        self.x9.setText(_translate("MainWindow", "X9-"))
        self.x10.setText(_translate("MainWindow", "X10-"))
        self.x11.setText(_translate("MainWindow", "X11-"))
        self.x12.setText(_translate("MainWindow", "X12-"))
        self.x13.setText(_translate("MainWindow", "X13-"))
        self.tabBar2.setTabText(self.tabBar2.indexOf(self.tab), _translate("MainWindow", "Registor"))
        self.tabBar2.setTabText(self.tabBar2.indexOf(self.tab_2), _translate("MainWindow", "Memory"))
        self.tabBar.setTabText(self.tabBar.indexOf(self.Simulator), _translate("MainWindow", "Simulator"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPreferences.setTitle(_translate("MainWindow", "Preferences"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.Open.setText(_translate("MainWindow", "Open File"))
        self.Open.setStatusTip(_translate("MainWindow", "Open a file"))
        self.Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.Save.setText(_translate("MainWindow", "Save File"))
        self.Save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.generate.setText(_translate("MainWindow", "Generate mc file"))
        self.generate.setStatusTip(_translate("MainWindow", "Click to generate machine code file"))
        self.generate.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.Clear_Output.setText(_translate("MainWindow", "Clear Output"))
        self.Clear_Output.setStatusTip(_translate("MainWindow", "Clears Output Browser"))
        self.Clear_Output.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.README.setText(_translate("MainWindow", "README"))
        self.README.setStatusTip(_translate("MainWindow", "want some help!!!"))
        self.README.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.Enable_P.setText(_translate("MainWindow", "Enable Pipelining"))
        self.EnabledD.setText(_translate("MainWindow", "Enabled"))
        self.menuData_Forwarding.setTitle(_translate("MainWindow", "Data Forwarding"))

        self.Open.triggered.connect(self.open_file)
        self.Save.triggered.connect(self.save_file)
        self.generate.triggered.connect(self.generate_file)
        self.Exit.triggered.connect(lambda:self.Exit_code(MainWindow))
        self.Run.clicked.connect(self.run_code)
        self.Step.clicked.connect(self.step_code)
        self.Clear.clicked.connect(self.clear_output)
        self.Prev.clicked.connect(self.prev_code)
        self.Clear_Output.triggered.connect(self.clear_output)
        self.Breakpoint.clicked.connect(self.break_point)
        MainWindow.setWindowTitle(_translate("MainWindow", "RISC-V Simulator"))
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.Reset.clicked.connect(self.reset_code)
        self.README.triggered.connect(self.readme_window)
        self.output.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.knode1=False
        self.knode2=False
        self.first=True
        self.Enable_P.changed.connect(self.runpipeline)
        self.EnabledD.changed.connect(self.dataforwarding)
        
    def runpipeline(self):
        self.knode1=not self.knode1
    def dataforwarding(self):
        self.knode2=not self.knode2
        

    def selectionchange(self,i):
        if(i==0):
            self.t1.setText(str(main3.RegList[main3.count]['x1']))
            self.t0.setText(str(main3.RegList[main3.count]['x0']))
            self.t2.setText(str(main3.RegList[main3.count]['x2']))
            self.t3.setText(str(main3.RegList[main3.count]['x3']))
            self.t4.setText(str(main3.RegList[main3.count]['x4']))
            self.t5.setText(str(main3.RegList[main3.count]['x5']))
            self.t6.setText(str(main3.RegList[main3.count]['x6']))
            self.t7.setText(str(main3.RegList[main3.count]['x7']))
            self.t8.setText(str(main3.RegList[main3.count]['x8']))
            self.t9.setText(str(main3.RegList[main3.count]['x9']))
            self.t10.setText(str(main3.RegList[main3.count]['x10']))
            self.t11.setText(str(main3.RegList[main3.count]['x11']))
            self.t12.setText(str(main3.RegList[main3.count]['x12']))
            self.t13.setText(str(main3.RegList[main3.count]['x13']))
            self.t14.setText(str(main3.RegList[main3.count]['x14']))
            self.t15.setText(str(main3.RegList[main3.count]['x15']))
            self.t16.setText(str(main3.RegList[main3.count]['x16']))
            self.t17.setText(str(main3.RegList[main3.count]['x17']))
            self.t18.setText(str(main3.RegList[main3.count]['x18']))
            self.t19.setText(str(main3.RegList[main3.count]['x19']))
            self.t20.setText(str(main3.RegList[main3.count]['x20']))
            self.t21.setText(str(main3.RegList[main3.count]['x21']))
            self.t22.setText(str(main3.RegList[main3.count]['x22']))
            self.t23.setText(str(main3.RegList[main3.count]['x23']))
            self.t24.setText(str(main3.RegList[main3.count]['x24']))
            self.t25.setText(str(main3.RegList[main3.count]['x25']))
            self.t26.setText(str(main3.RegList[main3.count]['x26']))
            self.t27.setText(str(main3.RegList[main3.count]['x27']))
            self.t28.setText(str(main3.RegList[main3.count]['x28']))
            self.t29.setText(str(main3.RegList[main3.count]['x29']))
            self.t30.setText(str(main3.RegList[main3.count]['x30']))
            self.t31.setText(str(main3.RegList[main3.count]['x31'])) 
        if(i==1):
            self.t1.setText(str(hex(main3.RegList[main3.count]['x1'])))
            #self.t1.setText("0x"+str(hex(main3.RegList[main3.count]['x1']).replace("0x","").rjust(8,'0')))
            self.t0.setText(str(hex(main3.RegList[main3.count]['x0'])))
            self.t2.setText(str(hex(main3.RegList[main3.count]['x2'])))
            self.t3.setText(str(hex(main3.RegList[main3.count]['x3'])))
            self.t4.setText(str(hex(main3.RegList[main3.count]['x4'])))
            self.t5.setText(str(hex(main3.RegList[main3.count]['x5'])))
            self.t6.setText(str(hex(main3.RegList[main3.count]['x6'])))
            self.t7.setText(str(hex(main3.RegList[main3.count]['x7'])))
            self.t8.setText(str(hex(main3.RegList[main3.count]['x8'])))
            self.t9.setText(str(hex(main3.RegList[main3.count]['x9'])))
            self.t10.setText(str(hex(main3.RegList[main3.count]['x10'])))
            self.t11.setText(str(hex(main3.RegList[main3.count]['x11'])))
            self.t12.setText(str(hex(main3.RegList[main3.count]['x12'])))
            self.t13.setText(str(hex(main3.RegList[main3.count]['x13'])))
            self.t14.setText(str(hex(main3.RegList[main3.count]['x14'])))
            self.t15.setText(str(hex(main3.RegList[main3.count]['x15'])))
            self.t16.setText(str(hex(main3.RegList[main3.count]['x16'])))
            self.t17.setText(str(hex(main3.RegList[main3.count]['x17'])))
            self.t18.setText(str(hex(main3.RegList[main3.count]['x18'])))
            self.t19.setText(str(hex(main3.RegList[main3.count]['x19'])))
            self.t20.setText(str(hex(main3.RegList[main3.count]['x20'])))
            self.t21.setText(str(hex(main3.RegList[main3.count]['x21'])))
            self.t22.setText(str(hex(main3.RegList[main3.count]['x22'])))
            self.t23.setText(str(hex(main3.RegList[main3.count]['x23'])))
            self.t24.setText(str(hex(main3.RegList[main3.count]['x24'])))
            self.t25.setText(str(hex(main3.RegList[main3.count]['x25'])))
            self.t26.setText(str(hex(main3.RegList[main3.count]['x26'])))
            self.t27.setText(str(hex(main3.RegList[main3.count]['x27'])))
            self.t28.setText(str(hex(main3.RegList[main3.count]['x28'])))
            self.t29.setText(str(hex(main3.RegList[main3.count]['x29'])))
            self.t30.setText(str(hex(main3.RegList[main3.count]['x30'])))
            self.t31.setText(str(hex(main3.RegList[main3.count]['x31']))) 
        
    def clear_output(self):
        self.output.clear()
    def Exit_code(self,MainWindow):
        MainWindow.close()   
        
    def generate_file(self):
        with open("input.txt",'w') as f:
            file_text2=self.Edit.toPlainText()
            f.write(file_text2)
        f.close()
        main1("input.txt")
        main3.main3()
        #MainWindow.close()   

        
       # main3.main3()
        main3.count=0
        with open("output.mc",'r') as r:
            file_text2=r.read()
            self.machine_code.setText(file_text2)
        self.machine_code.setEnabled(False)
        self.Simulator.setEnabled(True)

        
        
    def save_file(self):
        filename1=QFileDialog.getSaveFileName(os.getenv('Desktop'))
        with open(filename1[0],'w') as f:
            file_text2=self.Edit.toPlainText()
            f.write(file_text2)
            
            
    def open_file(self):
        filename = QFileDialog.getOpenFileName(os.getenv('Desktop'))
        path=filename[0]
        print(path)
        
        with open(path,'r') as f:
            file_text=f.read()
            self.Edit.setText(file_text) 
        main1("input.txt")
        main3.main3()
        with open("output.mc",'r') as b:
            file_text1=b.read()
            self.machine_code.setText(file_text1)
        self.machine_code.setEnabled(False)
        self.Simulator.setEnabled(True)
        
        
    def run_code(self):
        if self.knode1:
            print("Checked")
        main3.count = main3.InstCount
        main3.clock = main3.InstCount 
        self.t1.setText(str(main3.RegList[main3.count]['x1']))
        self.t0.setText(str(main3.RegList[main3.count]['x0']))
        self.t2.setText(str(main3.RegList[main3.count]['x2']))
        self.t3.setText(str(main3.RegList[main3.count]['x3']))
        self.t4.setText(str(main3.RegList[main3.count]['x4']))
        self.t5.setText(str(main3.RegList[main3.count]['x5']))
        self.t6.setText(str(main3.RegList[main3.count]['x6']))
        self.t7.setText(str(main3.RegList[main3.count]['x7']))
        self.t8.setText(str(main3.RegList[main3.count]['x8']))
        self.t9.setText(str(main3.RegList[main3.count]['x9']))
        self.t10.setText(str(main3.RegList[main3.count]['x10']))
        self.t11.setText(str(main3.RegList[main3.count]['x11']))
        self.t12.setText(str(main3.RegList[main3.count]['x12']))
        self.t13.setText(str(main3.RegList[main3.count]['x13']))
        self.t14.setText(str(main3.RegList[main3.count]['x14']))
        self.t15.setText(str(main3.RegList[main3.count]['x15']))
        self.t16.setText(str(main3.RegList[main3.count]['x16']))
        self.t17.setText(str(main3.RegList[main3.count]['x17']))
        self.t18.setText(str(main3.RegList[main3.count]['x18']))
        self.t19.setText(str(main3.RegList[main3.count]['x19']))
        self.t20.setText(str(main3.RegList[main3.count]['x20']))
        self.t21.setText(str(main3.RegList[main3.count]['x21']))
        self.t22.setText(str(main3.RegList[main3.count]['x22']))
        self.t23.setText(str(main3.RegList[main3.count]['x23']))
        self.t24.setText(str(main3.RegList[main3.count]['x24']))
        self.t25.setText(str(main3.RegList[main3.count]['x25']))
        self.t26.setText(str(main3.RegList[main3.count]['x26']))
        self.t27.setText(str(main3.RegList[main3.count]['x27']))
        self.t28.setText(str(main3.RegList[main3.count]['x28']))
        self.t29.setText(str(main3.RegList[main3.count]['x29']))
        self.t30.setText(str(main3.RegList[main3.count]['x30']))
        self.t31.setText(str(main3.RegList[main3.count]['x31'])) 
        #self.memory.append("PCList-"+str(PCList))
        self.Run.setEnabled(False)
        self.Step.setEnabled(False)
        self.Breakpoint.setEnabled(False)
        self.Prev.setEnabled(False)
        self.Clear.setEnabled(False)
        self.breakline.setEnabled(False)
        self.output.append("---------------------------------------------------------------------------------")
        self.output.append(">>Current PC-"+str(main3.PCList[main3.count]))
        self.output.append(">>Clock-"+str(main3.clock))
        TepMem=main3.MemList[main3.count]
        self.memory.setText(str(TempMem))
        self.output.append("---------------------------------------------------------------------------------")

    def setLineFormat(self,lineN,format):
        
        cursor = QtGui.QTextCursor(self.machine_code.document().findBlockByLineNumber(lineN))
        cursor.setBlockFormat(format)
        
    def break_point(self):
        main3.count=int(self.breakline.text())
        if main3.count>main3.InstCount:
            self.output.append("---------------------------------------------------------------------------------")
            self.output.append("Out of Range")
            self.output.append("---------------------------------------------------------------------------------")
        else:
            self.t1.setText(str(main3.RegList[main3.count]['x1']))
            self.t0.setText(str(main3.RegList[main3.count]['x0']))
            self.t2.setText(str(main3.RegList[main3.count]['x2']))
            self.t3.setText(str(main3.RegList[main3.count]['x3']))
            self.t4.setText(str(main3.RegList[main3.count]['x4']))
            self.t5.setText(str(main3.RegList[main3.count]['x5']))
            self.t6.setText(str(main3.RegList[main3.count]['x6']))
            self.t7.setText(str(main3.RegList[main3.count]['x7']))
            self.t8.setText(str(main3.RegList[main3.count]['x8']))
            self.t9.setText(str(main3.RegList[main3.count]['x9']))
            self.t10.setText(str(main3.RegList[main3.count]['x10']))
            self.t11.setText(str(main3.RegList[main3.count]['x11']))
            self.t12.setText(str(main3.RegList[main3.count]['x12']))
            self.t13.setText(str(main3.RegList[main3.count]['x13']))
            self.t14.setText(str(main3.RegList[main3.count]['x14']))
            self.t15.setText(str(main3.RegList[main3.count]['x15']))
            self.t16.setText(str(main3.RegList[main3.count]['x16']))
            self.t17.setText(str(main3.RegList[main3.count]['x17']))
            self.t18.setText(str(main3.RegList[main3.count]['x18']))
            self.t19.setText(str(main3.RegList[main3.count]['x19']))
            self.t20.setText(str(main3.RegList[main3.count]['x20']))
            self.t21.setText(str(main3.RegList[main3.count]['x21']))
            self.t22.setText(str(main3.RegList[main3.count]['x22']))
            self.t23.setText(str(main3.RegList[main3.count]['x23']))
            self.t24.setText(str(main3.RegList[main3.count]['x24']))
            self.t25.setText(str(main3.RegList[main3.count]['x25']))
            self.t26.setText(str(main3.RegList[main3.count]['x26']))
            self.t27.setText(str(main3.RegList[main3.count]['x27']))
            self.t28.setText(str(main3.RegList[main3.count]['x28']))
            self.t29.setText(str(main3.RegList[main3.count]['x29']))
            self.t30.setText(str(main3.RegList[main3.count]['x30']))
            self.t31.setText(str(main3.RegList[main3.count]['x31']))
            self.Run.setEnabled(False)
            self.Step.setEnabled(False)
            self.Breakpoint.setEnabled(False)
            self.Prev.setEnabled(False)
            self.Clear.setEnabled(False)
            self.breakline.setEnabled(False)
            self.output.append("---------------------------------------------------------------------------------")
            self.output.append(">>Current PC-"+str(main3.PCList[main3.count]))
            self.output.append(">>Clock-"+str(main3.clock))
            TepMem=main3.MemList[main3.count]
            self.memory.setText(str(TempMem))
            self.output.append("---------------------------------------------------------------------------------")

        #self.memory.append("PCList-"+str(PCList))
        
        
        
    def step_code(self):
        fmt = QtGui.QTextCharFormat()
        fmt2 = QtGui.QTextCharFormat()
        color=True
        if color:
            fmt.clearBackground()
            fmt.setForeground(QtCore.Qt.black)
            fmt.setBackground(QtCore.Qt.black)
            fmt.setForeground(QtCore.Qt.white)
        else:
            fmt.setBackground(QtCore.Qt.white)
        block = self.machine_code.document().findBlockByLineNumber(main3.PCList[main3.count]/4)
        blockPos = block.position()
        block2 = self.machine_code.document().findBlockByLineNumber(main3.PCList[main3.count]/4-1)
        blockPos2 = block2.position()

        cursor = QtGui.QTextCursor(self.machine_code.document())
        cursor.setPosition(blockPos)
        cursor.select(QtGui.QTextCursor.LineUnderCursor)
        cursor.setCharFormat(fmt)
        cursor = QtGui.QTextCursor(self.machine_code.document())
        cursor.setPosition(blockPos2)
        cursor.select(QtGui.QTextCursor.LineUnderCursor)
        cursor.setCharFormat(fmt2)

        main3.count = main3.count if main3.count >= main3.InstCount else main3.count + 1
        '''
        format=QtGui.QTextBlockFormat()
        format.clearBackground()
        self.setLineFormat((main3.PCList[main3.count]/4,format)
        format.setBackground(QtCore.Qt.black)
        '''
        self.t1.setText(str(main3.RegList[main3.count]['x1']))
        self.t0.setText(str(main3.RegList[main3.count]['x0']))
        self.t2.setText(str(main3.RegList[main3.count]['x2']))
        self.t3.setText(str(main3.RegList[main3.count]['x3']))
        self.t4.setText(str(main3.RegList[main3.count]['x4']))
        self.t5.setText(str(main3.RegList[main3.count]['x5']))
        self.t6.setText(str(main3.RegList[main3.count]['x6']))
        self.t7.setText(str(main3.RegList[main3.count]['x7']))
        self.t8.setText(str(main3.RegList[main3.count]['x8']))
        self.t9.setText(str(main3.RegList[main3.count]['x9']))
        self.t10.setText(str(main3.RegList[main3.count]['x10']))
        self.t11.setText(str(main3.RegList[main3.count]['x11']))
        self.t12.setText(str(main3.RegList[main3.count]['x12']))
        self.t13.setText(str(main3.RegList[main3.count]['x13']))
        self.t14.setText(str(main3.RegList[main3.count]['x14']))
        self.t15.setText(str(main3.RegList[main3.count]['x15']))
        self.t16.setText(str(main3.RegList[main3.count]['x16']))
        self.t17.setText(str(main3.RegList[main3.count]['x17']))
        self.t18.setText(str(main3.RegList[main3.count]['x18']))
        self.t19.setText(str(main3.RegList[main3.count]['x19']))
        self.t20.setText(str(main3.RegList[main3.count]['x20']))
        self.t21.setText(str(main3.RegList[main3.count]['x21']))
        self.t22.setText(str(main3.RegList[main3.count]['x22']))
        self.t23.setText(str(main3.RegList[main3.count]['x23']))
        self.t24.setText(str(main3.RegList[main3.count]['x24']))
        self.t25.setText(str(main3.RegList[main3.count]['x25']))
        self.t26.setText(str(main3.RegList[main3.count]['x26']))
        self.t27.setText(str(main3.RegList[main3.count]['x27']))
        self.t28.setText(str(main3.RegList[main3.count]['x28']))
        self.t29.setText(str(main3.RegList[main3.count]['x29']))
        self.t30.setText(str(main3.RegList[main3.count]['x30']))
        self.t31.setText(str(main3.RegList[main3.count]['x31']))
        main3.clock = main3.clock + 1 if main3.clock < main3.InstCount else main3.clock
        self.output.append("---------------------------------------------------------------------------------")
        self.output.append(">>Current PC-"+str(main3.PCList[main3.count]))
        self.output.append(">>Clock-"+str(main3.clock))
        TepMem=main3.MemList[main3.count]
        self.memory.setText(str(TempMem))
        self.output.append("---------------------------------------------------------------------------------")
        print(main3.PCList[main3.count])
        self.first=True
        self.Run.setEnabled(False)
        
        
    def prev_code(self):
        if self.first:
            main3.count = main3.count - 1
            self.first=False
        else:
           main3.count = main3.count if main3.count <= 0 else main3.count - 1 
        fmt = QtGui.QTextCharFormat()
        fmt2 = QtGui.QTextCharFormat()
        color=True
        if color:
            fmt.clearBackground()
            fmt.setForeground(QtCore.Qt.black)
            fmt.setBackground(QtCore.Qt.black)
            fmt.setForeground(QtCore.Qt.white)
        else:
            fmt.setBackground(QtCore.Qt.white)
        block = self.machine_code.document().findBlockByLineNumber(main3.PCList[main3.count]/4-1)
        blockPos = block.position()
        block2 = self.machine_code.document().findBlockByLineNumber(main3.PCList[main3.count]/4)
        blockPos2 = block2.position()

        cursor = QtGui.QTextCursor(self.machine_code.document())
        cursor.setPosition(blockPos)
        cursor.select(QtGui.QTextCursor.LineUnderCursor)
        cursor.setCharFormat(fmt)
        cursor = QtGui.QTextCursor(self.machine_code.document())
        cursor.setPosition(blockPos2)
        cursor.select(QtGui.QTextCursor.LineUnderCursor)
        cursor.setCharFormat(fmt2)
    
        
        self.t1.setText(str(main3.RegList[main3.count]['x1']))
        self.t0.setText(str(main3.RegList[main3.count]['x0']))
        self.t2.setText(str(main3.RegList[main3.count]['x2']))
        self.t3.setText(str(main3.RegList[main3.count]['x3']))
        self.t4.setText(str(main3.RegList[main3.count]['x4']))
        self.t5.setText(str(main3.RegList[main3.count]['x5']))
        self.t6.setText(str(main3.RegList[main3.count]['x6']))
        self.t7.setText(str(main3.RegList[main3.count]['x7']))
        self.t8.setText(str(main3.RegList[main3.count]['x8']))
        self.t9.setText(str(main3.RegList[main3.count]['x9']))
        self.t10.setText(str(main3.RegList[main3.count]['x10']))
        self.t11.setText(str(main3.RegList[main3.count]['x11']))
        self.t12.setText(str(main3.RegList[main3.count]['x12']))
        self.t13.setText(str(main3.RegList[main3.count]['x13']))
        self.t14.setText(str(main3.RegList[main3.count]['x14']))
        self.t15.setText(str(main3.RegList[main3.count]['x15']))
        self.t16.setText(str(main3.RegList[main3.count]['x16']))
        self.t17.setText(str(main3.RegList[main3.count]['x17']))
        self.t18.setText(str(main3.RegList[main3.count]['x18']))
        self.t19.setText(str(main3.RegList[main3.count]['x19']))
        self.t20.setText(str(main3.RegList[main3.count]['x20']))
        self.t21.setText(str(main3.RegList[main3.count]['x21']))
        self.t22.setText(str(main3.RegList[main3.count]['x22']))
        self.t23.setText(str(main3.RegList[main3.count]['x23']))
        self.t24.setText(str(main3.RegList[main3.count]['x24']))
        self.t25.setText(str(main3.RegList[main3.count]['x25']))
        self.t26.setText(str(main3.RegList[main3.count]['x26']))
        self.t27.setText(str(main3.RegList[main3.count]['x27']))
        self.t28.setText(str(main3.RegList[main3.count]['x28']))
        self.t29.setText(str(main3.RegList[main3.count]['x29']))
        self.t30.setText(str(main3.RegList[main3.count]['x30']))
        self.t31.setText(str(main3.RegList[main3.count]['x31']))
        main3.clock = main3.clock - 1 if main3.clock > 0 else main3.clock
        self.output.append("---------------------------------------------------------------------------------")
        self.output.append(">>Current PC-"+str(PCList[main3.count]))
        self.output.append(">>Clock-"+str(main3.clock))
        TempMem=main3.MemList[main3.count]
        self.memory.setText(str(TempMem))
        self.output.append("---------------------------------------------------------------------------------")
        
        
        
        
    def reset_code(self):
        main3.count=0
        self.output.clear()
        self.t1.setText(str(main3.RegList[main3.count]['x1']))
        self.t0.setText(str(main3.RegList[main3.count]['x0']))
        self.t2.setText(str(main3.RegList[main3.count]['x2']))
        self.t3.setText(str(main3.RegList[main3.count]['x3']))
        self.t4.setText(str(main3.RegList[main3.count]['x4']))
        self.t5.setText(str(main3.RegList[main3.count]['x5']))
        self.t6.setText(str(main3.RegList[main3.count]['x6']))
        self.t7.setText(str(main3.RegList[main3.count]['x7']))
        self.t8.setText(str(main3.RegList[main3.count]['x8']))
        self.t9.setText(str(main3.RegList[main3.count]['x9']))
        self.t10.setText(str(main3.RegList[main3.count]['x10']))
        self.t11.setText(str(main3.RegList[main3.count]['x11']))
        self.t12.setText(str(main3.RegList[main3.count]['x12']))
        self.t13.setText(str(main3.RegList[main3.count]['x13']))
        self.t14.setText(str(main3.RegList[main3.count]['x14']))
        self.t15.setText(str(main3.RegList[main3.count]['x15']))
        self.t16.setText(str(main3.RegList[main3.count]['x16']))
        self.t17.setText(str(main3.RegList[main3.count]['x17']))
        self.t18.setText(str(main3.RegList[main3.count]['x18']))
        self.t19.setText(str(main3.RegList[main3.count]['x19']))
        self.t20.setText(str(main3.RegList[main3.count]['x20']))
        self.t21.setText(str(main3.RegList[main3.count]['x21']))
        self.t22.setText(str(main3.RegList[main3.count]['x22']))
        self.t23.setText(str(main3.RegList[main3.count]['x23']))
        self.t24.setText(str(main3.RegList[main3.count]['x24']))
        self.t25.setText(str(main3.RegList[main3.count]['x25']))
        self.t26.setText(str(main3.RegList[main3.count]['x26']))
        self.t27.setText(str(main3.RegList[main3.count]['x27']))
        self.t28.setText(str(main3.RegList[main3.count]['x28']))
        self.t29.setText(str(main3.RegList[main3.count]['x29']))
        self.t30.setText(str(main3.RegList[main3.count]['x30']))
        self.t31.setText(str(main3.RegList[main3.count]['x31']))
        self.Run.setEnabled(True)
        self.Step.setEnabled(True)
        self.Breakpoint.setEnabled(True)
        self.Prev.setEnabled(True)
        self.Clear.setEnabled(True)
        self.breakline.setEnabled(True)
        self.memory.clear()
        with open("output.mc",'r') as b:
            file_text1=b.read()
            self.machine_code.setText(file_text1)
        
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

