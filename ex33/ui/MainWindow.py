# Form implementation generated from reading ui file 'E:\QTDESIGN\K234112E\chap2\ex33\ui\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 566)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 751, 111))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEditOriginal = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditOriginal.setGeometry(QtCore.QRect(30, 40, 681, 51))
        self.lineEditOriginal.setObjectName("lineEditOriginal")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 150, 751, 111))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEditResult = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditResult.setGeometry(QtCore.QRect(30, 40, 681, 51))
        self.lineEditResult.setObjectName("lineEditResult")
        self.pushButtonRandom = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonRandom.setGeometry(QtCore.QRect(20, 280, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonRandom.setFont(font)
        self.pushButtonRandom.setObjectName("pushButtonRandom")
        self.pushButtonSmallest = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSmallest.setGeometry(QtCore.QRect(410, 280, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonSmallest.setFont(font)
        self.pushButtonSmallest.setObjectName("pushButtonSmallest")
        self.pushButtonSumArray = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSumArray.setGeometry(QtCore.QRect(20, 340, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonSumArray.setFont(font)
        self.pushButtonSumArray.setObjectName("pushButtonSumArray")
        self.pushButtonCountOdd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonCountOdd.setGeometry(QtCore.QRect(20, 400, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonCountOdd.setFont(font)
        self.pushButtonCountOdd.setObjectName("pushButtonCountOdd")
        self.pushButtonSumOdd = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonSumOdd.setGeometry(QtCore.QRect(20, 460, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonSumOdd.setFont(font)
        self.pushButtonSumOdd.setObjectName("pushButtonSumOdd")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 340, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButtonAsc = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonAsc.setGeometry(QtCore.QRect(410, 400, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonAsc.setFont(font)
        self.pushButtonAsc.setObjectName("pushButtonAsc")
        self.pushButtonDesc = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonDesc.setGeometry(QtCore.QRect(410, 460, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonDesc.setFont(font)
        self.pushButtonDesc.setObjectName("pushButtonDesc")
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
        self.groupBox.setTitle(_translate("MainWindow", "Original Array:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Result:"))
        self.pushButtonRandom.setText(_translate("MainWindow", "Random Array"))
        self.pushButtonSmallest.setText(_translate("MainWindow", "Smallest element"))
        self.pushButtonSumArray.setText(_translate("MainWindow", "Sum of Array"))
        self.pushButtonCountOdd.setText(_translate("MainWindow", "Count odd element"))
        self.pushButtonSumOdd.setText(_translate("MainWindow", "Sum of odd element"))
        self.pushButton_6.setText(_translate("MainWindow", "Increment double value"))
        self.pushButtonAsc.setText(_translate("MainWindow", "Sort - Ascending"))
        self.pushButtonDesc.setText(_translate("MainWindow", "Sort - Descending"))
