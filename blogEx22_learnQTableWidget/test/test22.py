from PyQt6.QtWidgets import QApplication, QMainWindow

from chap5_gui.blogEx22_learnQTableWidget.ui.MainWindow22Ex import MainWindow22Ex

app=QApplication([])
myWindow=MainWindow22Ex()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()