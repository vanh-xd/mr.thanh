from PyQt6.QtWidgets import QApplication, QMainWindow

from chap3.ex59.ui.MainWindow59Ex import MainWindow59Ex

app = QApplication([])
mainwindow = QMainWindow()
myui = MainWindow59Ex()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()