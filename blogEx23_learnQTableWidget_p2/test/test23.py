from PyQt6.QtWidgets import QApplication, QMainWindow

from chap5_gui.blogEx23_learnQTableWidget_p2.ui.MainWindow23Ex import MainWindow23Ex

app=QApplication([])
myWindow=MainWindow23Ex()
myWindow.setupUi(QMainWindow())
myWindow.showWindow()
app.exec()