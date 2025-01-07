from PyQt6.QtWidgets import QApplication, QMainWindow

from chap1_function.ex23.ui.MainWindow23Ex import MainWindow23Ex

app = QApplication([])
mainwindow = QMainWindow()
myui = MainWindow23Ex()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()