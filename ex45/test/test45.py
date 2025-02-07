from PyQt6.QtWidgets import QApplication, QMainWindow

from chap2.ex45.ui.MainWindow45Ex import MainWindow45Ex

app = QApplication([])
mainwindow = QMainWindow()
myui = MainWindow45Ex()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()