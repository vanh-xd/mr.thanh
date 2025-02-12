from PyQt6.QtWidgets import QApplication, QMainWindow

from chap3.ex63.ui.MainWindow63Ex import MainWindow63Ex

app = QApplication([])
mainwindow = QMainWindow()
myui = MainWindow63Ex()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()