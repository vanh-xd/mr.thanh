# Form implementation generated from reading ui file 'E:\QTDESIGN\K234112E\chap6\ex118\ui\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(738, 387)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditInput.setGeometry(QtCore.QRect(20, 10, 701, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditInput.setFont(font)
        self.lineEditInput.setObjectName("lineEditInput")
        self.pushButtonPlotData = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonPlotData.setGeometry(QtCore.QRect(20, 50, 701, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonPlotData.setFont(font)
        self.pushButtonPlotData.setObjectName("pushButtonPlotData")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 100, 701, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.myLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.myLayout.setContentsMargins(0, 0, 0, 0)
        self.myLayout.setObjectName("myLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 738, 26))
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
        self.pushButtonPlotData.setText(_translate("MainWindow", "PLOT DATA"))
