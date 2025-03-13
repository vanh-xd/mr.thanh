from PyQt6.QtWidgets import QApplication, QMainWindow

from chap6.TichHopChart.ui.MainWindowTHChartEx import MainWindowTHChartEx

app = QApplication([])
myWindow = MainWindowTHChartEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()