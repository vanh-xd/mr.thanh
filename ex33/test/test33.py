from PyQt6.QtWidgets import QApplication, QMainWindow

from chap2.ex33.ui.MaInWindow33Ex import MainWindow33Ex

app = QApplication([])
mainwindow = QMainWindow()
myui = MainWindow33Ex()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()