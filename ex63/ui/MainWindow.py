# Form implementation generated from reading ui file 'E:\QTDESIGN\K234112E\chap3\ex63\ui\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 652)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(194, 158, 255);\n"
"color: rgb(160, 255, 101);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 90, 351, 321))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.groupBox)
        self.scrollArea.setGeometry(QtCore.QRect(20, 40, 311, 261))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 309, 259))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayoutButton = QtWidgets.QVBoxLayout()
        self.verticalLayoutButton.setObjectName("verticalLayoutButton")
        self.verticalLayout_3.addLayout(self.verticalLayoutButton)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 90, 391, 361))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 101, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 101, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 101, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 121, 41))
        self.label_5.setObjectName("label_5")
        self.lineEditID = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditID.setGeometry(QtCore.QRect(150, 40, 231, 41))
        self.lineEditID.setObjectName("lineEditID")
        self.lineEditName = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditName.setGeometry(QtCore.QRect(150, 90, 231, 41))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditPrice = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditPrice.setGeometry(QtCore.QRect(150, 140, 231, 41))
        self.lineEditPrice.setObjectName("lineEditPrice")
        self.lineEditDiscount = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditDiscount.setGeometry(QtCore.QRect(150, 190, 231, 41))
        self.lineEditDiscount.setObjectName("lineEditDiscount")
        self.radioButtonOfficial = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButtonOfficial.setGeometry(QtCore.QRect(60, 250, 121, 31))
        self.radioButtonOfficial.setObjectName("radioButtonOfficial")
        self.radioButtonNotOfficial = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButtonNotOfficial.setGeometry(QtCore.QRect(220, 250, 161, 31))
        self.radioButtonNotOfficial.setObjectName("radioButtonNotOfficial")
        self.pushButtonSave = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonSave.setGeometry(QtCore.QRect(70, 290, 121, 41))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonRemove = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonRemove.setGeometry(QtCore.QRect(220, 290, 121, 41))
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 450, 761, 141))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButtonSearchName = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonSearchName.setGeometry(QtCore.QRect(550, 40, 181, 41))
        self.pushButtonSearchName.setObjectName("pushButtonSearchName")
        self.pushButtonFilterPrice = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonFilterPrice.setGeometry(QtCore.QRect(570, 90, 161, 41))
        self.pushButtonFilterPrice.setObjectName("pushButtonFilterPrice")
        self.lineEditEnterName = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.lineEditEnterName.setGeometry(QtCore.QRect(200, 40, 231, 41))
        self.lineEditEnterName.setObjectName("lineEditEnterName")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(30, 40, 141, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(30, 90, 141, 41))
        self.label_7.setObjectName("label_7")
        self.lineEditEnterPrice = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.lineEditEnterPrice.setGeometry(QtCore.QRect(200, 90, 231, 41))
        self.lineEditEnterPrice.setObjectName("lineEditEnterPrice")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 26))
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
        self.label.setText(_translate("MainWindow", "Product Management"))
        self.groupBox.setTitle(_translate("MainWindow", "Products:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Product Details:"))
        self.label_2.setText(_translate("MainWindow", "ID:"))
        self.label_3.setText(_translate("MainWindow", "Name:"))
        self.label_4.setText(_translate("MainWindow", "Price:"))
        self.label_5.setText(_translate("MainWindow", "Discount:"))
        self.radioButtonOfficial.setText(_translate("MainWindow", "Official"))
        self.radioButtonNotOfficial.setText(_translate("MainWindow", "Not Official"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.pushButtonRemove.setText(_translate("MainWindow", "Remove"))
        self.groupBox_3.setTitle(_translate("MainWindow", "More Functions:"))
        self.pushButtonSearchName.setText(_translate("MainWindow", "Search Name"))
        self.pushButtonFilterPrice.setText(_translate("MainWindow", "Filter Price"))
        self.label_6.setText(_translate("MainWindow", "Enter Name:"))
        self.label_7.setText(_translate("MainWindow", "Enter Price:"))
