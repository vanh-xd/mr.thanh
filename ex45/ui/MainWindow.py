# Form implementation generated from reading ui file 'E:\QTDESIGN\K234112E\chap2\ex45\ui\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 686)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 85, 255);\n"
"background-color: rgb(170, 170, 127);")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 100, 371, 521))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.groupBox)
        self.scrollArea.setGeometry(QtCore.QRect(20, 40, 331, 461))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 329, 459))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayoutBook = QtWidgets.QVBoxLayout()
        self.verticalLayoutBook.setObjectName("verticalLayoutBook")
        self.verticalLayout_2.addLayout(self.verticalLayoutBook)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(400, 100, 381, 351))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 91, 41))
        self.label_2.setObjectName("label_2")
        self.lineEditISBN = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditISBN.setGeometry(QtCore.QRect(140, 40, 151, 41))
        self.lineEditISBN.setObjectName("lineEditISBN")
        self.lineEditTitle = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditTitle.setGeometry(QtCore.QRect(140, 90, 151, 41))
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 91, 41))
        self.label_3.setObjectName("label_3")
        self.lineEditAuthor = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditAuthor.setGeometry(QtCore.QRect(140, 140, 151, 41))
        self.lineEditAuthor.setObjectName("lineEditAuthor")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 91, 41))
        self.label_4.setObjectName("label_4")
        self.lineEditYear = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditYear.setGeometry(QtCore.QRect(140, 190, 151, 41))
        self.lineEditYear.setObjectName("lineEditYear")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 91, 41))
        self.label_5.setObjectName("label_5")
        self.lineEditPublisher = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditPublisher.setGeometry(QtCore.QRect(140, 240, 151, 41))
        self.lineEditPublisher.setObjectName("lineEditPublisher")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 240, 121, 41))
        self.label_6.setObjectName("label_6")
        self.pushButtonSave = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonSave.setGeometry(QtCore.QRect(60, 290, 93, 41))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonRemove = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonRemove.setGeometry(QtCore.QRect(180, 290, 111, 41))
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(400, 460, 381, 161))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButtonSearchTitle = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonSearchTitle.setGeometry(QtCore.QRect(20, 40, 161, 41))
        self.pushButtonSearchTitle.setObjectName("pushButtonSearchTitle")
        self.pushButtonSearchISBN = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonSearchISBN.setGeometry(QtCore.QRect(20, 90, 161, 41))
        self.pushButtonSearchISBN.setObjectName("pushButtonSearchISBN")
        self.pushButtonFilterYears = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonFilterYears.setGeometry(QtCore.QRect(210, 40, 141, 41))
        self.pushButtonFilterYears.setObjectName("pushButtonFilterYears")
        self.pushButtonFilterPublisher = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonFilterPublisher.setGeometry(QtCore.QRect(190, 90, 181, 41))
        self.pushButtonFilterPublisher.setObjectName("pushButtonFilterPublisher")
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
        self.label.setText(_translate("MainWindow", "Book Managements"))
        self.groupBox.setTitle(_translate("MainWindow", "Books:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Book Details:"))
        self.label_2.setText(_translate("MainWindow", "ISBN:"))
        self.label_3.setText(_translate("MainWindow", "Title:"))
        self.label_4.setText(_translate("MainWindow", "Author:"))
        self.label_5.setText(_translate("MainWindow", "Year:"))
        self.label_6.setText(_translate("MainWindow", "Publisher:"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.pushButtonRemove.setText(_translate("MainWindow", "Remove"))
        self.groupBox_3.setTitle(_translate("MainWindow", "More functions:"))
        self.pushButtonSearchTitle.setText(_translate("MainWindow", "Search Title"))
        self.pushButtonSearchISBN.setText(_translate("MainWindow", "Search ISBN"))
        self.pushButtonFilterYears.setText(_translate("MainWindow", "Filter Years"))
        self.pushButtonFilterPublisher.setText(_translate("MainWindow", "Filter Publisher"))
