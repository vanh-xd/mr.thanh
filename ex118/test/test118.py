from PyQt6.QtWidgets import QApplication, QMainWindow

from chap6.ex118.ui.MainWindow118Ex import MainWindow118Ex

app = QApplication([])
myWindow = MainWindow118Ex()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()