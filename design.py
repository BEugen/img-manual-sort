# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1159, 745)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.gridWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridWidget.setGeometry(QtCore.QRect(0, 0, 1151, 711))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.source = QtWidgets.QPushButton(self.gridWidget)
        self.source.setObjectName("source")
        self.horizontalLayout.addWidget(self.source)
        self.destination = QtWidgets.QPushButton(self.gridWidget)
        self.destination.setObjectName("destination")
        self.horizontalLayout.addWidget(self.destination)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.img_full = QtWidgets.QLabel(self.gridWidget)
        self.img_full.setText("")
        self.img_full.setObjectName("img_full")
        self.verticalLayout.addWidget(self.img_full)
        self.count = QtWidgets.QLabel(self.gridWidget)
        self.count.setAlignment(QtCore.Qt.AlignCenter)
        self.count.setObjectName("count")
        self.verticalLayout.addWidget(self.count)
        self.pb0 = QtWidgets.QPushButton(self.gridWidget)
        self.pb0.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pb0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pb0.setAutoRepeatInterval(100)
        self.pb0.setObjectName("pb0")
        self.verticalLayout.addWidget(self.pb0)
        self.pb1 = QtWidgets.QPushButton(self.gridWidget)
        self.pb1.setMinimumSize(QtCore.QSize(0, 50))
        self.pb1.setObjectName("pb1")
        self.verticalLayout.addWidget(self.pb1)
        self.pb2 = QtWidgets.QPushButton(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb2.sizePolicy().hasHeightForWidth())
        self.pb2.setSizePolicy(sizePolicy)
        self.pb2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pb2.setObjectName("pb2")
        self.verticalLayout.addWidget(self.pb2)
        self.pb3 = QtWidgets.QPushButton(self.gridWidget)
        self.pb3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pb3.setObjectName("pb3")
        self.verticalLayout.addWidget(self.pb3)
        self.pb4 = QtWidgets.QPushButton(self.gridWidget)
        self.pb4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pb4.setObjectName("pb4")
        self.verticalLayout.addWidget(self.pb4)
        self.pb5 = QtWidgets.QPushButton(self.gridWidget)
        self.pb5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pb5.setObjectName("pb5")
        self.verticalLayout.addWidget(self.pb5)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.img = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img.sizePolicy().hasHeightForWidth())
        self.img.setSizePolicy(sizePolicy)
        self.img.setMinimumSize(QtCore.QSize(1000, 700))
        self.img.setScaledContents(True)
        self.img.setObjectName("img")
        self.gridLayout.addWidget(self.img, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.source.setText(_translate("MainWindow", "Source"))
        self.destination.setText(_translate("MainWindow", "Destination"))
        self.count.setText(_translate("MainWindow", "0"))
        self.pb0.setText(_translate("MainWindow", "Empty (0)"))
        self.pb1.setText(_translate("MainWindow", "Low material (1)"))
        self.pb2.setText(_translate("MainWindow", "Dust (2)"))
        self.pb3.setText(_translate("MainWindow", "Briket + Dust (3)"))
        self.pb4.setText(_translate("MainWindow", "Broken br.(4)"))
        self.pb5.setText(_translate("MainWindow", "Briket (5)"))
        self.img.setText(_translate("MainWindow", "TextLabel"))

