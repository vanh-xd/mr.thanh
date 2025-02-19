from PyQt6.QtWidgets import QApplication, QMainWindow

from chap4.ex85.ui.LoginMainWindow85Ex import LoginMainWindow85Ex

app = QApplication([])
mainwindow = QMainWindow()
myui = LoginMainWindow85Ex()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()