from PyQt6.QtWidgets import QApplication, QMainWindow

from chap2.ex39.ui.MainWindow39Ex import MainWindow39Ex

app = QApplication([])
mainwindow = QMainWindow()
myui = MainWindow39Ex()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()