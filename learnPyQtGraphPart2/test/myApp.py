from PyQt6.QtWidgets import QApplication, QMainWindow
from chap6.learnPyQtGraphPart2.ui.MainWindowGraph2Ex import MainWindowGraph2Ex

app = QApplication([])
myWindow = MainWindowGraph2Ex()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()