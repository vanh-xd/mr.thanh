from chap6.learnPyQtGraphPart1.ui.MainWindow import Ui_MainWindow
import pyqtgraph as pg

class MainWindowGraph1Ex(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.graphWidget = pg.PlotWidget()
        hour = [1,2,3,4,5,6,7,8,9,10,11,12]
        temperature = [20,21,20,32,33,31,29,31,32,35,37,45]
        self.graphWidget.plot(hour, temperature)
        self.myLayout.addWidget(self.graphWidget)
    def show(self):
        self.MainWindow.show()