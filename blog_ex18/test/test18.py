from PyQt6.QtWidgets import QApplication, QMainWindow

from chap5_gui.blog_ex18.ui.MainWindow18Ex import MainWindow18Ex

app = QApplication([])
mainwindow = QMainWindow()
myui = MainWindow18Ex()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()