from PyQt6.QtWidgets import QApplication, QMainWindow

from chap1_function.ex21.ui.MainWindow21Ex import MainWindowEx21

app = QApplication([])
mainwindow = QMainWindow()
myui = MainWindowEx21()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()