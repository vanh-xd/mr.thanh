from PyQt6.QtWidgets import QMessageBox, QMainWindow

from chap4.ex85.libs.DataConnector import DataConnector
from chap4.ex85.ui.AssetMainWindowEx import AssetMainWindowEx
from chap4.ex85.ui.LoginMainWindow import Ui_MainWindow


class LoginMainWindow85Ex(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)
    def process_login(self):
        uid = self.lineEditUserName.text()
        pwd = self.lineEditPassword.text()
        dc = DataConnector()
        emp = dc.login(uid, pwd)
        if emp == None:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText('login failed')
            self.msg.exec()
        else:
            self.MainWindow.close()
            self.mainwindow = QMainWindow()
            self.myui = AssetMainWindowEx()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()