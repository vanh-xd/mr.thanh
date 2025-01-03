from PyQt6.QtWidgets import QApplication, QMainWindow

from chap1_function.ex22.ui.MainWindow22Ex import MainWindow22Ex

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow22Ex()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()