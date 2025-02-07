from PyQt6.QtWidgets import QApplication, QMainWindow

from chap2.ex38.ui.MainWindow38Ex import MainWindow38Ex

app = QApplication([])
mainwindow = QMainWindow()
myui = MainWindow38Ex()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()