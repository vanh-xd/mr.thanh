from PyQt6.QtWidgets import QApplication, QMainWindow

from chap1_function.ex24_baikho.ui.MainWindow24Ex import MainWindow24Ex

app = QApplication([])
mainwindow = QMainWindow()
myui = MainWindow24Ex()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()