from PyQt6.QtWidgets import QApplication, QMainWindow

from chap3.ex64.ui.MainWindow64Ex import MainWindow64Ex

app = QApplication([])
mainwindow = QMainWindow()
myui = MainWindow64Ex()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()