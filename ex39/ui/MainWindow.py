# Form implementation generated from reading ui file 'E:\QTDESIGN\K234112E\chap2\ex39\ui\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 816)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEditNumber = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditNumber.setGeometry(QtCore.QRect(110, 100, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEditNumber.setFont(font)
        self.lineEditNumber.setObjectName("lineEditNumber")
        self.pushButtonRandom = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonRandom.setGeometry(QtCore.QRect(330, 90, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonRandom.setFont(font)
        self.pushButtonRandom.setObjectName("pushButtonRandom")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(40, 180, 481, 541))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 479, 539))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayoutButton = QtWidgets.QVBoxLayout()
        self.verticalLayoutButton.setObjectName("verticalLayoutButton")
        self.verticalLayout_2.addLayout(self.verticalLayoutButton)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButtonAdd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(540, 170, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonAdd.setFont(font)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonUpdate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonUpdate.setGeometry(QtCore.QRect(540, 250, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonUpdate.setFont(font)
        self.pushButtonUpdate.setObjectName("pushButtonUpdate")
        self.pushButtonDelete = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonDelete.setGeometry(QtCore.QRect(540, 330, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonDelete.setFont(font)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.pushButtonAscSort = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAscSort.setGeometry(QtCore.QRect(540, 410, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonAscSort.setFont(font)
        self.pushButtonAscSort.setObjectName("pushButtonAscSort")
        self.pushButtonDescSort = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonDescSort.setGeometry(QtCore.QRect(540, 490, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonDescSort.setFont(font)
        self.pushButtonDescSort.setObjectName("pushButtonDescSort")
        self.pushButtonRemove = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonRemove.setGeometry(QtCore.QRect(540, 570, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonRemove.setFont(font)
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "List Operations"))
        self.label_2.setText(_translate("MainWindow", "N:"))
        self.lineEditNumber.setText(_translate("MainWindow", "50"))
        self.pushButtonRandom.setText(_translate("MainWindow", "Create Random"))
        self.pushButtonAdd.setText(_translate("MainWindow", "Add"))
        self.pushButtonUpdate.setText(_translate("MainWindow", "Update"))
        self.pushButtonDelete.setText(_translate("MainWindow", "Delete"))
        self.pushButtonAscSort.setText(_translate("MainWindow", "Asc Sort"))
        self.pushButtonDescSort.setText(_translate("MainWindow", "Desc Sort"))
        self.pushButtonRemove.setText(_translate("MainWindow", "Remove All"))
