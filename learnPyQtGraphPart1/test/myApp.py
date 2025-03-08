from PyQt6.QtWidgets import QApplication, QMainWindow

from chap6.learnPyQtGraphPart1.ui.MainWindowGraph1EX import MainWindowGraph1Ex

app = QApplication([])
myWindow = MainWindowGraph1Ex()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()