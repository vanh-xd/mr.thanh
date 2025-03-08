from PyQt6.QtWidgets import QApplication, QMainWindow

from chap6.ex117.ui.MainWindow117Ex import MainWindow117Ex

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow117Ex()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()