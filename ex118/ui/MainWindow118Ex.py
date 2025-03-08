from chap6.ex118.ui.MainWindow import Ui_MainWindow
import pyqtgraph as pg
import numpy as np

class MainWindow118Ex(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.MainWindow.setWindowTitle('Banh Beo - Data Plotter')
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground('k')
        self.myLayout.addWidget(self.graphWidget)
        self.setupSignalAndSlot()
    def show(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonPlotData.clicked.connect(self.plotData)

    def plotData(self):
        input = self.lineEditInput.text()
        input = input.replace(';', ',')
        data_array = np.array([float(x.strip()) for x in input.split(',') if x.strip()])

        x_values = np.arange(len(data_array))

        pen = pg.mkPen(color='blue', width=2)
        self.graphWidget.plot(x_values, data_array, pen=pen, symbol='o', symbolSize=10, symbolBrush='blue')

        self.graphWidget.setYRange(-10, 30)
        self.graphWidget.setXRange(-1, 7)
