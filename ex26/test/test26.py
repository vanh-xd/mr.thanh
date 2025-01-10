from PyQt6.QtWidgets import QApplication, QMainWindow

from chap2.ex26.ui.MainWindow26Ex import MainWindow26Ex

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow26Ex()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()